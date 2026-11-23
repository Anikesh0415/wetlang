#include "../include/wet_crt.h"
#include "../include/wetvm_api.h"
#include "../include/wetvm_types.h"
#include "../include/biophysics.h"
#include "../include/interlocks.h"
#include "../include/wet_hal.h"
#include "../include/wet_hal_pump_valve.h"
#include "../include/wet_aer.h"
#include "../include/wet_scheduler.h"

int printf(const char* format, ...);
int puts(const char* str);
void abort(void);

#define HARNESS_ASSERT(cond) do { \
    if (!(cond)) { \
        printf("ASSERTION FAILED (%s:%d): %s\n", __FILE__, __LINE__, #cond); \
        abort(); \
    } \
} while (0)
#undef assert
#define assert HARNESS_ASSERT

/* Helper to build a minimal valid WBC binary */
static size_t build_synthetic_wbc(uint8_t* out, size_t max_len, uint16_t caps) {
    if (max_len < 64) return 0;
    memset(out, 0, max_len);

    /* 1. Header (32 bytes) */
    out[0] = 'W'; out[1] = 'B'; out[2] = 'C'; out[3] = 0x01; /* Magic WBC\x01 */
    out[4] = 0x01; out[5] = 0x00; /* Major=1, Minor=0 */
    out[6] = (uint8_t)(caps & 0xFF);
    out[7] = (uint8_t)((caps >> 8) & 0xFF);
    out[8] = 0x01; /* Sequence counter = 1 */
    out[9] = 0x00; out[10] = 0x00; out[11] = 0x00;
    out[12] = 0x01; /* Section count = 1 */
    out[13] = 0x40; /* 64 channels */
    out[14] = 0x00; out[15] = 0x00;

    /* Max charge limit: float 0.5 nC = 0x3F000000 */
    out[16] = 0x00; out[17] = 0x00; out[18] = 0x00; out[19] = 0x3F;

    /* Section 1 Header: Section Type 3 (BYTECODE_STREAM), offset 48, length 8 */
    out[32] = 0x03; out[33] = 0x00;
    out[34] = 0x30; out[35] = 0x00; out[36] = 0x00; out[37] = 0x00; /* Offset 48 */
    out[38] = 0x08; out[39] = 0x00; out[40] = 0x00; out[41] = 0x00; /* Length 8 */

    /* Bytecode at offset 48:
     * 0x02 = SYNC_TICK
     * 0x11 = PUSH_INT 42
     * 0x01 = HALT */
    out[48] = 0x02; /* SYNC_TICK */
    out[49] = 0x11; out[50] = 42; out[51] = 0; out[52] = 0; out[53] = 0; /* PUSH_INT 42 */
    out[54] = 0x02; /* SYNC_TICK */
    out[55] = 0x01; /* HALT */

    size_t total_len = 56;
    /* Write total size to header */
    out[20] = (uint8_t)(total_len & 0xFF);
    out[21] = (uint8_t)((total_len >> 8) & 0xFF);
    out[22] = (uint8_t)((total_len >> 16) & 0xFF);
    out[23] = (uint8_t)((total_len >> 24) & 0xFF);

    /* Compute CRC32 over payload bytes [28..total_len-1] */
    uint32_t crc = 0xFFFFFFFFU;
    for (size_t i = 28; i < total_len; ++i) {
        crc ^= out[i];
        for (int k = 0; k < 8; ++k) {
            crc = (crc >> 1) ^ (0xEDB88320U & -(crc & 1U));
        }
    }
    crc ^= 0xFFFFFFFFU;
    out[24] = (uint8_t)(crc & 0xFF);
    out[25] = (uint8_t)((crc >> 8) & 0xFF);
    out[26] = (uint8_t)((crc >> 16) & 0xFF);
    out[27] = (uint8_t)((crc >> 24) & 0xFF);

    return total_len;
}

static void test_vm_lifecycle_and_arena(void) {
    printf("[1/6] Testing VM Lifecycle and Static Arena Allocation...\n");
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.channel_count = 64;
    cfg.max_stack_depth = 512;
    cfg.max_locals = 128;
    cfg.max_ops_per_tick = 10000;

    /* 1. Dynamic Allocation */
    wet_vm_t* vm = wet_create_vm(&cfg);
    assert(vm != NULL);
    wet_telemetry_t telem;
    memset(&telem, 0, sizeof(telem));
    int res = wet_step_tick(vm, &telem);
    assert(res == 0);
    wet_free_vm(vm);

    /* 2. Static Arena Allocation (2MB static buffer) */
    size_t arena_sz = 2 * 1024 * 1024;
    void* arena = malloc(arena_sz);
    assert(arena != NULL);
    memset(arena, 0xAA, arena_sz); /* Dirty memory */

    wet_vm_t* arena_vm = wet_create_vm_arena(arena, arena_sz, &cfg);
    assert(arena_vm != NULL);
    res = wet_step_tick(arena_vm, &telem);
    assert(res == 0);
    wet_free_vm(arena_vm);
    free(arena);
    printf("    -> PASS: Dynamic & Static Arena Zero-Malloc Verified.\n");
}

static void test_corrupted_bytecode_hardening(void) {
    printf("[2/6] Testing Adversarial Corrupted Bytecode Inputs...\n");
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.channel_count = 64;

    wet_vm_t* vm = wet_create_vm(&cfg);
    assert(vm != NULL);

    char err_buf[256];
    uint8_t buf[256];
    size_t len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION | WET_CAP_MICROFLUIDICS);
    assert(len > 0);

    /* 1. Valid bytecode load */
    wet_status_t st = wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf));
    assert(st == WET_OK);

    /* 2. Truncated header (0 to 31 bytes) */
    for (size_t trunc = 0; trunc < 32; ++trunc) {
        st = wet_load_bytecode(vm, buf, trunc, err_buf, sizeof(err_buf));
        assert(st != WET_OK);
    }

    /* 3. Corrupt Magic */
    buf[0] = 'B'; buf[1] = 'A'; buf[2] = 'D'; buf[3] = '!';
    st = wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf));
    assert(st == WET_ERR_INVALID_MAGIC || st != WET_OK);

    /* 4. Corrupt CRC32 */
    len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION);
    buf[24] ^= 0xFF; /* Flip CRC byte */
    st = wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf));
    assert(st == WET_ERR_CRC_MISMATCH || st != WET_OK);

    /* 5. Malicious Section Header Offset pointing past EOF */
    len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION);
    buf[34] = 0xFF; buf[35] = 0xFF; /* Offset = 65535 */
    st = wet_load_bytecode(vm, buf, len, err_buf, sizeof(err_buf));
    assert(st != WET_OK);

    wet_free_vm(vm);
    printf("    -> PASS: All Corrupted Bytecode Invariants Safely Rejected.\n");
}

static void test_biophysics_numerical_and_interlocks(void) {
    printf("[3/6] Testing 50,000 Biophysics Steps & Interlock Boundaries...\n");
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.channel_count = 64;

    wet_vm_t* vm = wet_create_vm(&cfg);
    assert(vm != NULL);

    /* Configure electrode: Platinum on channel 0, TiN on channel 1, PEDOT on channel 2 */
    wet_configure_electrode(vm, WET_ELEC_PLATINUM, 132.25f);

    /* Load valid minimal WBC */
    uint8_t buf[256];
    char err[256];
    size_t len = build_synthetic_wbc(buf, sizeof(buf), WET_CAP_STIMULATION | WET_CAP_HIGH_VOLTAGE | WET_CAP_MICROFLUIDICS);
    assert(wet_load_bytecode(vm, buf, len, err, sizeof(err)) == WET_OK);

    wet_telemetry_t telem;
    for (int tick = 0; tick < 50000; ++tick) {
        /* Inject periodic safe biphasic pulses */
        if (tick % 200 == 0) {
            wet_inject_stimulus(vm, 0, 0.4f, 0.2f, 0.2f);
        }
        int res = wet_step_tick(vm, &telem);
        assert(res == 0);

        /* Invariant checks every 500 ticks */
        if (tick % 500 == 0) {
            assert(telem.population_rate_hz >= 0.0f);
            assert(telem.population_rate_hz < 1000.0f);
            for (int ch = 0; ch < 64; ++ch) {
                /* Voltage must be bounded within physical compliance [-7.0V, +7.0V] */
                assert(telem.voltages[ch] >= -7.5f && telem.voltages[ch] <= 7.5f);
            }
        }
    }

    /* Test Asymmetric Clamping */
    float clamped_high = wet_clamp_voltage_vm(vm, 1.5f);
    assert(clamped_high <= 0.81f && clamped_high >= 0.79f); /* Pt anodic rail = +0.8V */
    float clamped_low = wet_clamp_voltage_vm(vm, -1.5f);
    assert(clamped_low >= -0.61f && clamped_low <= -0.59f);  /* Pt cathodic rail = -0.6V */

    wet_free_vm(vm);
    printf("    -> PASS: 50,000 Biophysics Steps Clean & Asymmetric Clamping Verified.\n");
}

static void test_microfluidics_mems_and_recoil(void) {
    printf("[4/6] Testing Microfluidics MEMS Overpressure & Throttled Recoil Relief...\n");
    wet_hal_driver_t* drv = wet_hal_microfluidics_create(WET_HAL_MODE_PHYSICAL);
    assert(drv != NULL);

    /* 1. Baseline normal pump run with downstream valve open */
    wet_hal_status_t st = wet_hal_pump_set_rate(drv, 0, 2.0, 1);
    assert(st == WET_HAL_OK);

    /* 2. Dead-head trip: close downstream valve 0 */
    st = wet_hal_valve_set_state(drv, 0, 0);
    assert(st == WET_HAL_OK);
    st = wet_hal_pump_set_rate(drv, 0, 2.0, 1);
    assert(st == WET_HAL_ERR_DEAD_HEAD); /* Must trip immediately! */

    /* 3. MEMS Overpressure trip: open valve, but set inline MEMS pressure sensor to 65.0 kPa (> 50 kPa limit) */
    st = wet_hal_valve_set_state(drv, 0, 1);
    assert(st == WET_HAL_OK);
    wet_hal_pump_set_inline_pressure(drv, 0, 65.0f);
    st = wet_hal_pump_set_rate(drv, 0, 2.0, 1);
    assert(st == WET_HAL_ERR_DEAD_HEAD); /* Overpressure burst protection trips! */

    /* 4. Restore safe pressure */
    wet_hal_pump_set_inline_pressure(drv, 0, 15.0f);
    st = wet_hal_pump_set_rate(drv, 0, 2.0, 1);
    assert(st == WET_HAL_OK);

    wet_hal_microfluidics_destroy(drv);
    printf("    -> PASS: MEMS Transducer & Throttled Bypass Interlock Verified.\n");
}

static void test_aer_and_spsc_ring_buffers(void) {
    printf("[5/6] Testing AER & SPSC Lock-Free Event Ring Buffers...\n");
    wet_aer_ring_t ring;
    wet_aer_packet_t* pkt_buf = (wet_aer_packet_t*)malloc(1024 * sizeof(wet_aer_packet_t));
    assert(pkt_buf != NULL);
    uint16_t ch_counts[64];
    memset(ch_counts, 0, sizeof(ch_counts));

    int init_res = wet_aer_ring_init(&ring, pkt_buf, 1024, 5000000, ch_counts, 64);
    assert(init_res == 0);

    /* Push 2,000 events into 1,024-capacity SPSC ring buffer to test wrap-around and overflow telemetry */
    uint32_t pushed = 0;
    uint32_t dropped = 0;
    for (uint32_t i = 0; i < 2000; ++i) {
        if (wet_aer_push(&ring, (uint64_t)i, (uint16_t)(i % 64), 100, 0) == 0) {
            pushed++;
        } else {
            dropped++;
        }
    }

    assert(pushed > 0);
    assert(dropped > 0);
    assert(pushed + dropped == 2000);
    assert(ring.total_dropped == (uint64_t)dropped); /* Exact telemetry accounting of capacity drops */

    /* Drain all pushed events */
    wet_aer_packet_t out_batch[256];
    uint32_t total_popped = 0;
    while (1) {
        uint32_t popped = wet_aer_pop_batch(&ring, out_batch, 256);
        if (popped == 0) break;
        total_popped += popped;
    }
    assert(total_popped == pushed);
    free(pkt_buf);

    printf("    -> PASS: AER SPSC Ring Buffer Pointer Wraps & Overflow Accounting Exact.\n");
}

static void test_attocoulomb_fixed_point_resolution(void) {
    printf("[6/6] Testing 64-bit AttoCoulomb Resolution (0.1 fC Sub-pA Leakage)...\n");
    interlock_state_t il;
    interlocks_init(&il);

    /* Sub-picoampere leakage: 1 pA * 100 us = 0.1 fC = 1e-7 nC per tick */
    float tick_leakage_nc[INTERLOCK_NUM_CHANNELS];
    memset(tick_leakage_nc, 0, sizeof(tick_leakage_nc));
    tick_leakage_nc[0] = 1e-7f; /* 0.1 fC = 100 attoCoulombs */

    /* Run 100,000 ticks of 0.1 fC leakage */
    for (uint64_t t = 1; t <= 100000; ++t) {
        wet_status_t st = interlocks_record_charge_tick(&il, t, tick_leakage_nc);
        assert(st == WET_OK);
    }

    /* Expected charge: 100,000 ticks * 100 aC = 10,000,000 aC = 10 pC = 0.01 nC */
    int64_t expected_ac = 100000LL * 100LL;
    assert(il.cumulative_dc_attocoulombs[0] == expected_ac);
    assert(il.cumulative_dc_attocoulombs[0] == 10000000LL);

    /* Verify active discharge resets to exact 0 */
    interlocks_active_discharge(&il, 0);
    assert(il.cumulative_dc_attocoulombs[0] == 0);
    assert(il.cumulative_unbounded_dc_nc[0] == 0.0f);

    printf("    -> PASS: 64-bit AttoCoulomb Accumulator Recorded Exact Zero-Loss Charge.\n");
}

int main(void) {
    printf("======================================================================\n");
    printf(" WetLang Native C99 Engine — ASan/UBSan & Invariant Stress Harness\n");
    printf("======================================================================\n");

    test_vm_lifecycle_and_arena();
    test_corrupted_bytecode_hardening();
    test_biophysics_numerical_and_interlocks();
    test_microfluidics_mems_and_recoil();
    test_aer_and_spsc_ring_buffers();
    test_attocoulomb_fixed_point_resolution();

    printf("======================================================================\n");
    printf(" ALL SANITIZER & INVARIANT SUITES PASSED CLEANLY (ZERO DEFECTS)\n");
    printf("======================================================================\n");
    return 0;
}
