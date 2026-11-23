#ifndef WET_BUILDING_DLL
#define WET_BUILDING_DLL
#endif

#include "../include/wet_crt.h"
#include "../include/wet_verification.h"
#include "../include/wetvm_types.h"
#include "../include/wetvm_api.h"
#include "../include/biophysics.h"
#include "../include/interlocks.h"
#include "../include/wet_hal.h"
#include "../include/wet_hal_pump_valve.h"
#include "../include/wet_aer.h"
#include "../include/wet_scheduler.h"

#if defined(_WIN32)
typedef void* HANDLE;
typedef unsigned long DWORD;
typedef int BOOL;

#ifdef __cplusplus
extern "C" {
#endif
HANDLE __stdcall CreateThread(void* lpThreadAttributes, size_t dwStackSize, void* lpStartAddress, void* lpParameter, DWORD dwCreationFlags, DWORD* lpThreadId);
DWORD  __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
BOOL   __stdcall CloseHandle(HANDLE hObject);
#ifdef __cplusplus
}
#endif
#else
#include <pthread.h>
#endif

extern uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc);

/* =========================================================================
 * Pillar 1: Sanitizer & Invariant Test Suite
 * ========================================================================= */

static size_t build_synthetic_wbc(uint8_t* out, size_t max_len, uint16_t caps) {
    if (max_len < 64) return 0;
    memset(out, 0, max_len);

    /* 1. Header (32 bytes): WETB format */
    out[0] = 'W'; out[1] = 'E'; out[2] = 'T'; out[3] = 'B'; /* Magic WETB */
    out[4] = 0x01; out[5] = 0x00; /* Version 1.0 */
    out[6] = (uint8_t)(caps & 0xFF);
    out[7] = (uint8_t)((caps >> 8) & 0xFF);

    uint32_t total_len = 56;
    out[8]  = (uint8_t)(total_len & 0xFF);
    out[9]  = (uint8_t)((total_len >> 8) & 0xFF);
    out[10] = (uint8_t)((total_len >> 16) & 0xFF);
    out[11] = (uint8_t)((total_len >> 24) & 0xFF);

    /* num_sections = 1 */
    out[16] = 0x01; out[17] = 0x00; out[18] = 0x00; out[19] = 0x00;
    /* sequence_counter = 1 */
    out[20] = 0x01; out[21] = 0x00; out[22] = 0x00; out[23] = 0x00;

    /* Section 1 Header: Section Type 3 (WET_SEC_BYTECODE_STREAM), offset 48, length 8 */
    out[32] = 0x03; out[33] = 0x00; /* sec_type = 3 */
    out[34] = 0x00; out[35] = 0x00;
    out[36] = 48;   out[37] = 0x00; out[38] = 0x00; out[39] = 0x00; /* sec_offset = 48 */
    out[40] = 8;    out[41] = 0x00; out[42] = 0x00; out[43] = 0x00; /* sec_size = 8 */

    /* Bytecode at offset 48:
     * 0x02 = SYNC_TICK
     * 0x11 = PUSH_INT 42
     * 0x02 = SYNC_TICK
     * 0x01 = HALT */
    out[48] = 0x02; /* SYNC_TICK */
    out[49] = 0x11; out[50] = 42; out[51] = 0; out[52] = 0; out[53] = 0; /* PUSH_INT 42 */
    out[54] = 0x02; /* SYNC_TICK */
    out[55] = 0x01; /* HALT */

    /* Compute CRC32: bytes 0..11, 4 zero bytes, bytes 16..total_len-1 */
    uint32_t crc = wet_compute_crc32(out, 12, 0);
    uint8_t zero_field[4] = {0, 0, 0, 0};
    crc = wet_compute_crc32(zero_field, 4, crc);
    crc = wet_compute_crc32(out + 16, total_len - 16, crc);

    out[12] = (uint8_t)(crc & 0xFF);
    out[13] = (uint8_t)((crc >> 8) & 0xFF);
    out[14] = (uint8_t)((crc >> 16) & 0xFF);
    out[15] = (uint8_t)((crc >> 24) & 0xFF);

    return total_len;
}

WET_EXPORT int wet_run_sanitizer_harness_c(wet_sanitizer_result_t* out_result) {
    if (!out_result) return -1;
    memset(out_result, 0, sizeof(*out_result));

    /* 1. Arena Allocation */
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.channel_count = 64;

    size_t arena_sz = 2 * 1024 * 1024;
    void* arena = malloc(arena_sz);
    if (!arena) return -2;
    memset(arena, 0xAA, arena_sz);

    wet_vm_t* arena_vm = wet_create_vm_arena(arena, arena_sz, &cfg);
    wet_telemetry_t telem;
    memset(&telem, 0, sizeof(telem));
    int res = wet_step_tick(arena_vm, &telem);
    wet_free_vm(arena_vm);
    free(arena);
    if (res == 0) out_result->arena_passed = 1;

    /* 2. Adversarial Corrupted Bytecode */
    wet_vm_t* vm = wet_create_vm(&cfg);
    if (!vm) return -3;
    char err_buf[256];
    uint8_t buf[256];
    size_t len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION | WET_CAP_MICROFLUIDICS);
    if (wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf)) == WET_OK) {
        int all_corrupt_rejected = 1;
        for (size_t trunc = 0; trunc < 32; ++trunc) {
            if (wet_load_bytecode(vm, buf, trunc, err_buf, sizeof(err_buf)) == WET_OK) {
                all_corrupt_rejected = 0;
            }
        }
        buf[0] = 'B'; buf[1] = 'A'; buf[2] = 'D'; buf[3] = '!';
        if (wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf)) == WET_OK) {
            all_corrupt_rejected = 0;
        }
        len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION);
        buf[12] ^= 0xFF; /* Bad CRC */
        if (wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf)) == WET_OK) {
            all_corrupt_rejected = 0;
        }
        if (all_corrupt_rejected) out_result->corrupted_bytecode_passed = 1;
    }

    /* 3. 50,000 Biophysics Steps & Asymmetric Clamping */
    wet_configure_electrode(vm, WET_ELEC_PLATINUM, 132.25f);
    len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION | WET_CAP_HIGH_VOLTAGE | WET_CAP_MICROFLUIDICS);
    if (wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf)) == WET_OK) {
        int bio_ok = 1;
        for (int tick = 0; tick < 50000; ++tick) {
            if (tick % 200 == 0) {
                wet_inject_stimulus(vm, 0, 0.4f, 0.2f, 0.2f);
            }
            if (wet_step_tick(vm, &telem) != 0) {
                bio_ok = 0;
                break;
            }
        }
        float chigh = wet_clamp_voltage_vm(vm, 1.5f);
        float clow  = wet_clamp_voltage_vm(vm, -1.5f);
        if (chigh > 0.79f && chigh < 0.81f && clow > -0.61f && clow < -0.59f && bio_ok) {
            out_result->biophysics_passed = 1;
        }
    }
    wet_free_vm(vm);

    /* 4. MEMS Transducer & Throttled Recoil Bypass */
    wet_hal_driver_t* drv = wet_hal_microfluidics_create(WET_HAL_MODE_PHYSICAL);
    if (drv) {
        int mems_ok = 1;
        if (wet_hal_pump_set_rate(drv, 0, 2.0, 1) != WET_HAL_OK) mems_ok = 0;
        wet_hal_valve_set_state(drv, 0, 0); /* Close valve -> dead head */
        if (wet_hal_pump_set_rate(drv, 0, 2.0, 1) != WET_HAL_ERR_DEAD_HEAD) mems_ok = 0;
        wet_hal_valve_set_state(drv, 0, 1); /* Open valve */
        wet_hal_pump_set_inline_pressure(drv, 0, 65.0f); /* Overpressure > 50 kPa */
        if (wet_hal_pump_set_rate(drv, 0, 2.0, 1) != WET_HAL_ERR_DEAD_HEAD) mems_ok = 0;
        wet_hal_pump_set_inline_pressure(drv, 0, 15.0f); /* Safe pressure */
        if (wet_hal_pump_set_rate(drv, 0, 2.0, 1) != WET_HAL_OK) mems_ok = 0;
        wet_hal_microfluidics_destroy(drv);
        if (mems_ok) out_result->mems_passed = 1;
    }

    /* 5. AER Ring Buffer Wrap & Overflow Accounting */
    wet_aer_ring_t ring;
    wet_aer_packet_t* pkt_buf = (wet_aer_packet_t*)malloc(1024 * sizeof(wet_aer_packet_t));
    if (pkt_buf) {
        uint16_t ch_counts[64];
        memset(ch_counts, 0, sizeof(ch_counts));
        wet_aer_ring_init(&ring, pkt_buf, 1024, 5000000, ch_counts, 64);
        uint32_t pushed = 0, dropped = 0;
        for (uint32_t i = 0; i < 2000; ++i) {
            if (wet_aer_push(&ring, (uint64_t)i, (uint16_t)(i % 64), 100, 0) == 0) pushed++;
            else dropped++;
        }
        wet_aer_packet_t drain_batch[256];
        uint32_t total_popped = 0;
        while (1) {
            uint32_t p = wet_aer_pop_batch(&ring, drain_batch, 256);
            if (p == 0) break;
            total_popped += p;
        }
        if (pushed + dropped == 2000 && ring.total_dropped == dropped && total_popped == pushed) {
            out_result->aer_passed = 1;
        }
        free(pkt_buf);
    }

    /* 6. 64-bit AttoCoulomb Resolution */
    interlock_state_t* il = (interlock_state_t*)calloc(1, sizeof(interlock_state_t));
    if (il) {
        interlocks_init(il);
        float tick_leakage_nc[INTERLOCK_NUM_CHANNELS];
        memset(tick_leakage_nc, 0, sizeof(tick_leakage_nc));
        tick_leakage_nc[0] = 1e-7f; /* 100 aC */
        for (uint64_t t = 1; t <= 100000; ++t) {
            interlocks_record_charge_tick(il, t, tick_leakage_nc);
        }
        int64_t expected_ac = 100000LL * 100LL;
        if (il->cumulative_dc_attocoulombs[0] == expected_ac && il->cumulative_dc_attocoulombs[0] == 10000000LL) {
            interlocks_active_discharge(il, 0);
            if (il->cumulative_dc_attocoulombs[0] == 0) {
                out_result->attocoulomb_passed = 1;
            }
        }
        free(il);
    }

    out_result->all_passed = (out_result->arena_passed &&
                              out_result->corrupted_bytecode_passed &&
                              out_result->biophysics_passed &&
                              out_result->mems_passed &&
                              out_result->aer_passed &&
                              out_result->attocoulomb_passed);
    return out_result->all_passed ? 0 : 1;
}

/* =========================================================================
 * Pillar 2: 10-Million Continuous Tick Numerical Soak Stress Test
 * ========================================================================= */

WET_EXPORT int wet_run_soak_10m_ticks(uint32_t total_ticks, wet_soak_result_t* out_result) {
    if (!out_result) return -1;
    memset(out_result, 0, sizeof(*out_result));

    uint64_t target_ticks = total_ticks > 0 ? (uint64_t)total_ticks : 10000000ULL;
    out_result->total_ticks = target_ticks;

    interlock_state_t* il = (interlock_state_t*)calloc(1, sizeof(interlock_state_t));
    bio_state_t* bio = (bio_state_t*)calloc(1, sizeof(bio_state_t));
    if (!il || !bio) {
        if (il) free(il);
        if (bio) free(bio);
        return -2;
    }

    interlocks_init(il);
    interlocks_configure_electrode(il, WET_ELEC_PLATINUM, 132.25f);
    biophysics_init(bio, 0.1, 987654321ULL);

    float tick_charge_nc[INTERLOCK_NUM_CHANNELS];

    int64_t theoretical_ac[INTERLOCK_NUM_CHANNELS];
    memset(theoretical_ac, 0, sizeof(theoretical_ac));

    int64_t max_drift_ac = 0;
    float min_v = 1e9f, max_v = -1e9f;
    uint32_t nan_or_inf = 0;

    const float pulse_phase_charge_nc = 0.0002f; /* 0.2 pC = 200,000 aC per tick */
    const int64_t pulse_phase_charge_ac = 200000LL;

    for (uint64_t t = 1; t <= target_ticks; ++t) {
        memset(tick_charge_nc, 0, sizeof(tick_charge_nc));

        /* Inject calibrated biphasic pulse every 250 ticks on channel 0 and 1 */
        uint64_t cycle_tick = t % 250;
        if (cycle_tick == 1 || cycle_tick == 2) {
            /* Cathodic phase: -0.4 V */
            tick_charge_nc[0] = -pulse_phase_charge_nc;
            tick_charge_nc[1] = -pulse_phase_charge_nc;
            theoretical_ac[0] -= pulse_phase_charge_ac;
            theoretical_ac[1] -= pulse_phase_charge_ac;
        } else if (cycle_tick == 3 || cycle_tick == 4) {
            /* Anodic phase: +0.4 V */
            tick_charge_nc[0] = pulse_phase_charge_nc;
            tick_charge_nc[1] = pulse_phase_charge_nc;
            theoretical_ac[0] += pulse_phase_charge_ac;
            theoretical_ac[1] += pulse_phase_charge_ac;
        }
        /* For cycle_tick >= 5 and cycle_tick == 0: quiescent, theoretical_ac is exactly 0 */

        /* Interlock charge recording */
        wet_status_t st = interlocks_record_charge_tick(il, t, tick_charge_nc);
        if (st != WET_OK) {
            out_result->interlock_trips++;
        }

        /* Schedule stimulus in biophysics digital twin */
        if (cycle_tick == 1) {
            biophysics_schedule_stim(bio, 0, 0.4f, 0.2f, 0.2f);
            biophysics_schedule_stim(bio, 1, 0.4f, 0.2f, 0.2f);
        }

        /* Biophysics ODE advancement */
        biophysics_step_tick(bio);

        /* Verify exact attoCoulomb accumulation every 1,000 ticks */
        if ((t % 1000) == 0) {
            for (int ch = 0; ch < 2; ++ch) {
                int64_t drift = il->cumulative_dc_attocoulombs[ch] - theoretical_ac[ch];
                if (drift < 0) drift = -drift;
                if (drift > max_drift_ac) {
                    max_drift_ac = drift;
                }
            }
        }

        /* Sample membrane voltages for physical boundedness and numerical stability */
        if ((t % 250) == 0) {
            for (int n = 0; n < BIO_NUM_NEURONS; ++n) {
                float v = bio->v_m_mv[n];
                if (v != v || v > 1000.0f || v < -1000.0f) {
                    nan_or_inf++;
                }
                if (v < min_v) min_v = v;
                if (v > max_v) max_v = v;
            }
        }
    }

    /* Final drift evaluation across all 64 channels */
    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        int64_t drift = il->cumulative_dc_attocoulombs[ch] - theoretical_ac[ch];
        if (drift < 0) drift = -drift;
        if (drift > max_drift_ac) {
            max_drift_ac = drift;
        }
        out_result->final_cumulative_dc_attocoulombs[ch] = il->cumulative_dc_attocoulombs[ch];
    }

    out_result->max_absolute_drift_attocoulombs = max_drift_ac;
    out_result->min_membrane_voltage_mv = min_v;
    out_result->max_membrane_voltage_mv = max_v;
    out_result->nan_or_inf_detected = nan_or_inf;

    int success = (max_drift_ac == 0 && nan_or_inf == 0 && out_result->interlock_trips == 0);
    free(il);
    free(bio);
    return success ? 0 : 1;
}

/* =========================================================================
 * Pillar 3: Multi-Threaded Concurrency & Lock-Free SPSC Queue Audit
 * ========================================================================= */

typedef struct {
    wet_aer_ring_t* ring;
    uint32_t        num_packets;
    uint32_t        thread_id;
    uint64_t        packets_done;
    uint64_t        torn_reads;
    uint64_t        sequence_errors;
} aer_thread_worker_t;

#if defined(_WIN32)
static DWORD __stdcall aer_producer_worker(void* param) {
    aer_thread_worker_t* w = (aer_thread_worker_t*)param;
    uint32_t count = w->num_packets;
    uint32_t tid = w->thread_id;
    wet_aer_ring_t* ring = w->ring;

    for (uint32_t i = 0; i < count; ++i) {
        uint64_t tick = ((uint64_t)i * 10ULL) + tid;
        uint16_t channel = (uint16_t)((i + tid) % 64);
        int16_t  amp_uv = (int16_t)(100 + (i % 500));
        uint16_t flags = (uint16_t)(i & 0x07);

        /* Spin-wait with pipeline pause if ring buffer is temporarily full */
        while (wet_aer_push(ring, tick, channel, amp_uv, flags) != 0) {
            wet_cpu_pause();
        }
    }
    w->packets_done = count;
    return 0;
}

static DWORD __stdcall aer_consumer_worker(void* param) {
    aer_thread_worker_t* w = (aer_thread_worker_t*)param;
    uint32_t target_count = w->num_packets;
    uint32_t tid = w->thread_id;
    wet_aer_ring_t* ring = w->ring;

    wet_aer_packet_t batch[64];
    uint32_t consumed = 0;

    while (consumed < target_count) {
        uint32_t popped = wet_aer_pop_batch(ring, batch, 64);
        if (popped == 0) {
            wet_cpu_pause();
            continue;
        }

        for (uint32_t k = 0; k < popped; ++k) {
            uint32_t expected_i = consumed + k;
            uint64_t exp_tick = ((uint64_t)expected_i * 10ULL) + tid;
            uint16_t exp_channel = (uint16_t)((expected_i + tid) % 64);
            int16_t  exp_amp = (int16_t)(100 + (expected_i % 500));
            uint16_t exp_flags = (uint16_t)(expected_i & 0x07);

            /* Check for torn reads / memory ordering violations */
            if (batch[k].timestamp_tick != exp_tick ||
                batch[k].channel_id != exp_channel ||
                batch[k].peak_amplitude_uv != exp_amp ||
                batch[k].flags != exp_flags) {
                w->torn_reads++;
            }
        }
        consumed += popped;
    }
    w->packets_done = consumed;
    return 0;
}
#endif

WET_EXPORT int wet_run_concurrency_stress(uint32_t total_packets, wet_concurrency_result_t* out_result) {
    if (!out_result) return -1;
    memset(out_result, 0, sizeof(*out_result));

    uint32_t target_packets = total_packets > 0 ? total_packets : 1000000U;
    /* Divide evenly across 2 independent SPSC channels (Producer 1 -> Consumer 1, Producer 2 -> Consumer 2) */
    uint32_t per_channel = target_packets / 2;

    wet_aer_packet_t* buf1 = (wet_aer_packet_t*)malloc(4096 * sizeof(wet_aer_packet_t));
    wet_aer_packet_t* buf2 = (wet_aer_packet_t*)malloc(4096 * sizeof(wet_aer_packet_t));
    if (!buf1 || !buf2) {
        if (buf1) free(buf1);
        if (buf2) free(buf2);
        return -2;
    }

    wet_aer_ring_t ring1, ring2;
    wet_aer_ring_init(&ring1, buf1, 4096, 50000000U, NULL, 0);
    wet_aer_ring_init(&ring2, buf2, 4096, 50000000U, NULL, 0);

    aer_thread_worker_t prod1 = { &ring1, per_channel, 1, 0, 0, 0 };
    aer_thread_worker_t cons1 = { &ring1, per_channel, 1, 0, 0, 0 };
    aer_thread_worker_t prod2 = { &ring2, per_channel, 2, 0, 0, 0 };
    aer_thread_worker_t cons2 = { &ring2, per_channel, 2, 0, 0, 0 };

#if defined(_WIN32)
    HANDLE threads[4];
    DWORD tid;
    threads[0] = CreateThread(NULL, 0, (void*)aer_consumer_worker, &cons1, 0, &tid);
    threads[1] = CreateThread(NULL, 0, (void*)aer_consumer_worker, &cons2, 0, &tid);
    threads[2] = CreateThread(NULL, 0, (void*)aer_producer_worker, &prod1, 0, &tid);
    threads[3] = CreateThread(NULL, 0, (void*)aer_producer_worker, &prod2, 0, &tid);

    for (int i = 0; i < 4; ++i) {
        if (threads[i]) {
            WaitForSingleObject(threads[i], 30000); /* Max 30 second timeout */
            CloseHandle(threads[i]);
        }
    }
#endif

    out_result->total_packets_produced = prod1.packets_done + prod2.packets_done;
    out_result->total_packets_consumed = cons1.packets_done + cons2.packets_done;
    out_result->torn_reads_detected = cons1.torn_reads + cons2.torn_reads;
    out_result->sequence_errors = cons1.sequence_errors + cons2.sequence_errors;
    out_result->num_threads = 4;

    free(buf1);
    free(buf2);

    int success = (out_result->total_packets_consumed == (uint64_t)target_packets &&
                   out_result->torn_reads_detected == 0 &&
                   out_result->sequence_errors == 0);
    return success ? 0 : 1;
}
