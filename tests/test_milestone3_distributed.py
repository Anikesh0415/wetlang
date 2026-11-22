"""
Milestone 3 Post-Audit Remediation Test Suite
Verifies:
1. 32-byte aligned TSN frame layout (sequence numbers, explicit release epoch, causality checks)
2. Slew-only IEEE 1588 PTP disciplining with stimulation safety inhibit (|residual_offset| <= 1000 ns)
3. 512-slot Hierarchical Timing Wheel eliminating Head-of-Line blocking for heterogeneous axonal delays
4. Late packet dropping and late drop telemetry
5. Cross-chamber epileptiform positive-feedback rate governor (>50 Hz trip)
6. Outbound TX stimulus artifact blanking suppression
"""

import struct
import numpy as np
import pytest
from bindings.distributed import (
    WetTSNFrame,
    WetPTPClock,
    WetTimingWheel,
    serialize_tsn_frame,
    validate_tsn_frame,
)


def test_tsn_frame_32byte_aligned_layout_and_causality():
    """Verify 32-byte aligned layout, sequence numbers, and causality validation."""
    src_epoch_ns = 1000000000
    rel_epoch_ns = 1005000000  # 5.0 ms axonal delay
    frame = serialize_tsn_frame(
        src_epoch_ns=src_epoch_ns,
        rel_epoch_ns=rel_epoch_ns,
        seq=101,
        src_chamb=1,
        dst_chamb=2,
        src_ch=15,
        dst_ch=42,
        amp_uv=-250,
        flags=0x0001,
    )

    assert bytes(frame).__len__() == 32
    assert validate_tsn_frame(frame, expected_dst_chamber=2)

    # Causality violation check: release epoch before source epoch
    violating_frame = serialize_tsn_frame(
        src_epoch_ns=1005000000,
        rel_epoch_ns=1000000000,  # Negative delay
        seq=102,
        src_chamb=1,
        dst_chamb=2,
        src_ch=1,
        dst_ch=1,
        amp_uv=-100,
    )
    assert not validate_tsn_frame(violating_frame, expected_dst_chamber=2)


def test_ptp_slew_only_disciplining_and_safety_inhibit():
    """
    Verify IEEE 1588 PTP slew-only disciplining:
    - Initially inhibits inter-chamber stimulation (stim_inhibited == True)
    - Disciplines residual offset below 1000 ns
    - Unlocks stimulation (stim_inhibited == False)
    """
    clk = WetPTPClock(kp=0.7, ki=0.2)
    assert not clk.is_synchronized
    assert clk.stim_inhibited, "Stimulation must be inhibited prior to clock synchronization"

    path_delay_ns = 150000
    initial_offset_ns = 25000

    for cycle in range(15):
        t1 = 1000000000 + (cycle * 100000000)
        t2 = t1 + path_delay_ns + initial_offset_ns
        t3 = t2 + 20000
        t4 = t3 + path_delay_ns - initial_offset_ns

        clk.update_offset(t1_ns=t1, t2_ns=t2, t3_ns=t3, t4_ns=t4)

    residual = abs(initial_offset_ns - clk.accumulated_offset_ns)
    assert clk.is_synchronized
    assert not clk.stim_inhibited, "Stimulation should be unlocked when residual <= 1000 ns"
    assert residual <= 1000


def test_timing_wheel_eliminates_head_of_line_blocking():
    """
    Critical test: Heterogeneous axonal delays must NOT experience head-of-line blocking!
    Schedule Spike A at t=0 with tau=40 ms (release at t=40 ms).
    Schedule Spike B at t=0 with tau=2 ms (release at t=2 ms).
    Spike B MUST pop at t=2 ms without waiting for Spike A!
    """
    tw = WetTimingWheel(chamber_id=2)
    current_time_ns = 1000000000  # t = 1.0 s

    # Spike A: tau = 40 ms (release at t + 40 ms)
    frame_a = serialize_tsn_frame(
        src_epoch_ns=current_time_ns,
        rel_epoch_ns=current_time_ns + 40000000,
        seq=1,
        src_chamb=1,
        dst_chamb=2,
        src_ch=10,
        dst_ch=20,
        amp_uv=-200,
    )
    assert tw.schedule(frame_a, current_time_ns) == 0

    # Spike B: tau = 2 ms (release at t + 2 ms)
    frame_b = serialize_tsn_frame(
        src_epoch_ns=current_time_ns,
        rel_epoch_ns=current_time_ns + 2000000,
        seq=2,
        src_chamb=1,
        dst_chamb=2,
        src_ch=5,
        dst_ch=15,
        amp_uv=-300,
    )
    assert tw.schedule(frame_b, current_time_ns) == 0

    # Step wheel to t + 2.0 ms (20 ticks of 100 us)
    sim_time = current_time_ns
    popped_b = []
    for _ in range(20):
        sim_time += 100000
        ready = tw.drain_tick(sim_time)
        popped_b.extend(ready)

    # Spike B MUST have popped at 2 ms! (Proving zero Head-of-Line blocking)
    assert len(popped_b) == 1
    assert popped_b[0].sequence_number == 2
    assert popped_b[0].source_channel == 5

    # Step wheel remaining 380 ticks to t + 40.0 ms
    popped_a = []
    for _ in range(380):
        sim_time += 100000
        ready = tw.drain_tick(sim_time)
        popped_a.extend(ready)

    assert len(popped_a) == 1
    assert popped_a[0].sequence_number == 1
    assert popped_a[0].source_channel == 10


def test_late_packet_drop_telemetry():
    """Verify packets arriving after their scheduled release epoch are safely dropped."""
    tw = WetTimingWheel(chamber_id=1)
    current_time_ns = 2000000000

    # Late packet: release epoch was 1.99 s, but current time is 2.00 s
    late_frame = serialize_tsn_frame(
        src_epoch_ns=1980000000,
        rel_epoch_ns=1990000000,
        seq=999,
        src_chamb=0,
        dst_chamb=1,
        src_ch=1,
        dst_ch=1,
        amp_uv=-100,
    )
    res = tw.schedule(late_frame, current_time_ns)
    assert res == -2  # Late drop code
    assert tw.late_drops == 1


def test_epileptiform_rate_governor_and_tx_blanking():
    """
    Verify:
    1. Cross-chamber rate governor halts runaway positive feedback if inter-chamber rate > 50 Hz.
    2. Outbound TX stimulus blanking suppresses phantom echo spikes.
    """
    tw = WetTimingWheel(chamber_id=0)
    current_time = 3000000000

    # 1. Test TX blanking suppression
    tw.set_tx_blanking(target_chamber=1, blanking_ticks=15)
    echo_frame = serialize_tsn_frame(
        src_epoch_ns=current_time,
        rel_epoch_ns=current_time + 5000000,
        seq=1,
        src_chamb=0,
        dst_chamb=1,
        src_ch=0,
        dst_ch=0,
        amp_uv=-150,
    )
    res = tw.schedule(echo_frame, current_time)
    assert res == -5, "TX stimulus artifact blanking should have suppressed echo frame"

    # 2. Test epileptiform runaway trip (> 50 spikes/sec to Chamber 2)
    for i in range(50):
        frame = serialize_tsn_frame(
            src_epoch_ns=current_time,
            rel_epoch_ns=current_time + 5000000,
            seq=100 + i,
            src_chamb=0,
            dst_chamb=2,
            src_ch=0,
            dst_ch=0,
            amp_uv=-150,
        )
        assert tw.schedule(frame, current_time) == 0

    # 51st frame within 1 second must trip the rate governor
    runaway_frame = serialize_tsn_frame(
        src_epoch_ns=current_time,
        rel_epoch_ns=current_time + 5000000,
        seq=151,
        src_chamb=0,
        dst_chamb=2,
        src_ch=0,
        dst_ch=0,
        amp_uv=-150,
    )
    res = tw.schedule(runaway_frame, current_time)
    assert res == -4, "Epileptiform rate governor should have tripped on >50 Hz rate"
    assert tw.is_epileptiform_tripped
