#ifndef WET_DISTRIBUTED_H
#define WET_DISTRIBUTED_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define WET_DIST_CACHELINE_SIZE 128
#define WET_TSN_FRAME_SIZE      32
#define WET_TIMING_WHEEL_SLOTS  512  /* 512 slots * 100 us = 51.2 ms horizon */
#define WET_WHEEL_BUCKET_CAP    64   /* Max spikes per 100 us tick */
#define WET_MAX_CHAMBERS        16

#if defined(_WIN32) || defined(__CYGWIN__)
  #ifdef WET_BUILDING_DLL
    #define WET_EXPORT __declspec(dllexport)
  #else
    #define WET_EXPORT __declspec(dllimport)
  #endif
#else
  #if defined(__GNUC__) && __GNUC__ >= 4
    #define WET_EXPORT __attribute__((visibility("default")))
  #else
    #define WET_EXPORT
  #endif
#endif

/*
 * Production 32-Byte Time-Sensitive Networking (TSN) Inter-Chamber Packet
 * Natural 8-byte alignment, zero split-load penalty, explicit release epoch & sequence number.
 */
#if defined(_MSC_VER)
#pragma pack(push, 8)
typedef struct {
    uint64_t source_epoch_ns;   /* 8 bytes: Originating biological spike epoch */
    uint64_t release_epoch_ns;  /* 8 bytes: Scheduled target delivery epoch */
    uint32_t sequence_number;   /* 4 bytes: Monotonic packet counter */
    uint16_t source_chamber;    /* 2 bytes: Originating incubator ID */
    uint16_t target_chamber;    /* 2 bytes: Destination incubator ID */
    uint16_t source_channel;    /* 2 bytes: Transmitting electrode */
    uint16_t target_channel;    /* 2 bytes: Receiving electrode */
    int16_t  spike_amplitude_uv;/* 2 bytes: Spike amplitude */
    uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: e-stop, bit 2: clock-sync, bit 3: echo-suppressed */
} wet_tsn_frame_t;
#pragma pack(pop)
#else
typedef struct __attribute__((aligned(8))) {
    uint64_t source_epoch_ns;   /* 8 bytes: Originating biological spike epoch */
    uint64_t release_epoch_ns;  /* 8 bytes: Scheduled target delivery epoch */
    uint32_t sequence_number;   /* 4 bytes: Monotonic packet counter */
    uint16_t source_chamber;    /* 2 bytes: Originating incubator ID */
    uint16_t target_chamber;    /* 2 bytes: Destination incubator ID */
    uint16_t source_channel;    /* 2 bytes: Transmitting electrode */
    uint16_t target_channel;    /* 2 bytes: Receiving electrode */
    int16_t  spike_amplitude_uv;/* 2 bytes: Spike amplitude */
    uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: e-stop, bit 2: clock-sync, bit 3: echo-suppressed */
} wet_tsn_frame_t;
#endif

#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
_Static_assert(sizeof(wet_tsn_frame_t) == 32, "wet_tsn_frame_t must be exactly 32 bytes");
#endif

/*
 * IEEE 1588 PTP Slew-Only Hardware Clock Disciplining State
 */
typedef struct {
    uint64_t local_time_ns;
    uint64_t grandmaster_time_ns;
    int64_t  accumulated_offset_ns;
    int64_t  mean_path_delay_ns;
    double   frequency_slew_ppm;
    double   integral_err_ns;
    double   kp;
    double   ki;
    uint8_t  is_synchronized;
    uint8_t  stim_inhibited;      /* Inhibited if |residual_offset| > 1000 ns */
    uint32_t sync_sequence;
} wet_ptp_clock_t;

/*
 * Timing Wheel Bucket for O(1) Heterogeneous Axonal Delay Dispatching
 * Eliminates Head-of-Line blocking inherent to FIFO queues.
 */
typedef struct {
    uint32_t count;
    wet_tsn_frame_t frames[WET_WHEEL_BUCKET_CAP];
} wet_timing_wheel_bucket_t;

typedef struct {
    wet_timing_wheel_bucket_t buckets[WET_TIMING_WHEEL_SLOTS];
    uint64_t current_wheel_tick;
    uint32_t chamber_id;
    uint64_t total_scheduled;
    uint64_t total_dispatched;
    uint64_t late_drops;
    uint64_t bucket_overflows;

    /* Cross-chamber epileptiform rate governor (caps max inter-chamber rate at 50 Hz) */
    uint32_t rate_governor_window_spikes;
    uint64_t rate_governor_last_tick;
    uint8_t  is_epileptiform_tripped;

    /* Outbound TX stimulus artifact blanking */
    uint32_t tx_blanking_ticks_remaining[WET_MAX_CHAMBERS];
} wet_timing_wheel_t;

/* PTP Clock Functions */
WET_EXPORT void wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki);
WET_EXPORT void wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns);
WET_EXPORT uint64_t wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns);

/* TSN Frame Functions */
WET_EXPORT int wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags);
WET_EXPORT int wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber);

/* Timing Wheel Functions */
WET_EXPORT int wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id);
WET_EXPORT int wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns);
WET_EXPORT uint32_t wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count);
WET_EXPORT void wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks);

#ifdef __cplusplus
}
#endif

#endif /* WET_DISTRIBUTED_H */
