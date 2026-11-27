#include "../include/wet_crt.h"
#include "../include/wetvm_types.h"
#include "../include/wetvm_api.h"

int printf(const char* format, ...);
int puts(const char* str);

#if defined(_WIN32) && defined(WET_NOSTDLIB_EXE)
int _fltused = 0x9875;
void __stdcall ExitProcess(unsigned int uExitCode);
int main(void);
void wet_c99_entry(void) {
    int rc = main();
    ExitProcess((unsigned int)rc);
}
#endif

static int g_failures = 0;

#define C99_CHECK(cond) do { \
    if (!(cond)) { \
        printf("FAIL (%s:%d): %s\n", __FILE__, __LINE__, #cond); \
        g_failures++; \
    } \
} while (0)

static float make_nan_f(void) {
    union { uint32_t u; float f; } v;
    v.u = 0x7FC00000U;
    return v.f;
}

static float make_pos_inf_f(void) {
    union { uint32_t u; float f; } v;
    v.u = 0x7F800000U;
    return v.f;
}

static float make_neg_inf_f(void) {
    union { uint32_t u; float f; } v;
    v.u = 0xFF800000U;
    return v.f;
}

static void write_u16_le(uint8_t* p, uint16_t v) {
    p[0] = (uint8_t)(v & 0xFFU);
    p[1] = (uint8_t)((v >> 8) & 0xFFU);
}

static void write_u32_le(uint8_t* p, uint32_t v) {
    p[0] = (uint8_t)(v & 0xFFU);
    p[1] = (uint8_t)((v >> 8) & 0xFFU);
    p[2] = (uint8_t)((v >> 16) & 0xFFU);
    p[3] = (uint8_t)((v >> 24) & 0xFFU);
}

static void write_f32_le(uint8_t* p, float v) {
    uint32_t bits = 0U;
    memcpy(&bits, &v, sizeof(bits));
    write_u32_le(p, bits);
}

static uint32_t c99_crc32(const uint8_t* data, size_t len) {
    uint32_t crc = 0xFFFFFFFFU;
    for (size_t i = 0; i < len; ++i) {
        crc ^= (i >= 12U && i < 16U) ? 0U : data[i];
        for (int k = 0; k < 8; ++k) {
            crc = (crc >> 1) ^ (0xEDB88320U & -(crc & 1U));
        }
    }
    return ~crc;
}

static size_t build_wbc_stream(
    uint8_t* out,
    size_t out_cap,
    uint16_t caps,
    const uint8_t* code,
    size_t code_len
) {
    size_t sec_hdr_off = WET_HEADER_SIZE;
    size_t code_off = WET_HEADER_SIZE + WET_SECTION_ENTRY_SIZE;
    size_t total = code_off + code_len;
    if (total > out_cap) return 0U;
    memset(out, 0, total);

    /* Header (32 bytes) */
    out[0] = 'W'; out[1] = 'E'; out[2] = 'T'; out[3] = 'B';
    out[4] = WET_VERSION_MAJOR;
    out[5] = WET_VERSION_MINOR;
    write_u16_le(out + 6, caps);
    write_u32_le(out + 8, (uint32_t)total);
    write_u32_le(out + 12, 0U);
    write_u32_le(out + 16, 1U); /* num_sections = 1 */
    write_u32_le(out + 20, 64U); /* channel_count = 64 */
    write_f32_le(out + 24, 0.5f); /* max_charge_nc */
    write_u32_le(out + 28, 1U); /* sequence_counter */

    /* Section 0: WET_SEC_BYTECODE_STREAM (type 3) */
    write_u16_le(out + sec_hdr_off, WET_SEC_BYTECODE_STREAM);
    write_u16_le(out + sec_hdr_off + 2, 0U);
    write_u32_le(out + sec_hdr_off + 4, (uint32_t)code_off);
    write_u32_le(out + sec_hdr_off + 8, (uint32_t)code_len);

    if (code_len > 0U && code != NULL) {
        memcpy(out + code_off, code, code_len);
    }

    uint32_t crc = c99_crc32(out, total);
    write_u32_le(out + 12, crc);
    return total;
}

typedef struct {
    wet_vm_t* vm;
    uint32_t  calls;
    uint32_t  blanked_ticks_seen;
    uint32_t  unblanked_ticks_after;
    uint8_t   spikes_during_blanking;
    uint8_t   seen_post_stim_zero_v;
    uint8_t   reentrant_cleared;
} hook_test_ctx_t;

static void hook_blanking_and_1000ticks(
    const wet_closed_loop_snapshot_t* snap,
    wet_closed_loop_cmd_t* out_cmd,
    void* user_data
) {
    hook_test_ctx_t* ctx = (hook_test_ctx_t*)user_data;
    ctx->calls++;

    if (snap->tick == 1ULL) {
        /* Trigger 0.1ms phase1 + 0.1ms phase2 on ch 0 (with 0.1ms post-stim blanking = 3 ticks total) */
        out_cmd->trigger = 1U;
        out_cmd->is_current = 0U;
        out_cmd->channel = 0U;
        out_cmd->amplitude = 0.5f;
        out_cmd->phase1_ms = 0.1f;
        out_cmd->phase2_ms = 0.1f;
        out_cmd->interphase_ms = 0.0f;
        return;
    }

    /* Ticks 2, 3 are active stim; tick 4 is the 1-tick (0.1ms) post-stim blanking tick */
    if (snap->tick >= 2ULL && snap->tick <= 4ULL) {
        if (snap->blanking_active[0] != 0U) {
            ctx->blanked_ticks_seen++;
        }
        if (snap->spikes[0] != 0U) {
            ctx->spikes_during_blanking++;
        }
        if (snap->tick == 4ULL && snap->voltages[0] == 0.0f) {
            ctx->seen_post_stim_zero_v = 1U;
        }
    } else if (snap->tick >= 5ULL && snap->tick <= 10ULL) {
        if (snap->blanking_active[0] == 0U) {
            ctx->unblanked_ticks_after++;
        }
    }
}

static void hook_reentrant_clear(
    const wet_closed_loop_snapshot_t* snap,
    wet_closed_loop_cmd_t* out_cmd,
    void* user_data
) {
    (void)out_cmd;
    hook_test_ctx_t* ctx = (hook_test_ctx_t*)user_data;
    ctx->calls++;
    if (snap->tick == 3ULL) {
        wet_status_t st = wet_register_closed_loop_hook(ctx->vm, NULL, NULL);
        if (st == WET_OK) {
            ctx->reentrant_cleared = 1U;
        }
    }
}

static void hook_shannon_violation(
    const wet_closed_loop_snapshot_t* snap,
    wet_closed_loop_cmd_t* out_cmd,
    void* user_data
) {
    (void)user_data;
    if (snap->tick == 1ULL) {
        out_cmd->trigger = 1U;
        out_cmd->is_current = 1U;
        out_cmd->channel = 1U;
        out_cmd->amplitude = 1000.0f; /* 1000 uA * 1 ms = 1 uC -> D=1e4 uC/cm2 -> log10(1e4)=4.0 > 1.75 */
        out_cmd->phase1_ms = 1.0f;
        out_cmd->phase2_ms = 1.0f;
        out_cmd->interphase_ms = 0.0f;
    }
}

static void hook_ref_bank_violation(
    const wet_closed_loop_snapshot_t* snap,
    wet_closed_loop_cmd_t* out_cmd,
    void* user_data
) {
    (void)user_data;
    if (snap->tick == 1ULL) {
        out_cmd->trigger = 1U;
        out_cmd->is_current = 0U;
        out_cmd->channel = 2U;
        out_cmd->amplitude = 0.4f;
        out_cmd->phase1_ms = 0.2f;
        out_cmd->phase2_ms = 0.2f;
        out_cmd->interphase_ms = 0.0f;
    }
}

static void hook_oob_channel(
    const wet_closed_loop_snapshot_t* snap,
    wet_closed_loop_cmd_t* out_cmd,
    void* user_data
) {
    (void)user_data;
    if (snap->tick == 1ULL) {
        out_cmd->trigger = 1U;
        out_cmd->is_current = 0U;
        out_cmd->channel = 70U;
        out_cmd->amplitude = 0.4f;
        out_cmd->phase1_ms = 0.2f;
        out_cmd->phase2_ms = 0.2f;
        out_cmd->interphase_ms = 0.0f;
    }
}

static void test_blanking_api_and_bytecode(void) {
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.max_stack_depth = 256;
    cfg.max_locals = 64;
    cfg.channel_count = 64;
    cfg.max_ops_per_tick = 10000;

    wet_vm_t* vm = wet_create_vm(&cfg);
    C99_CHECK(vm != NULL);

    /* Direct API boundary validation */
    C99_CHECK(wet_configure_blanking(NULL, 1.0f, 0) == WET_ERR_NULL_PTR);
    C99_CHECK(wet_configure_blanking(vm, 0.1f, 0) == WET_OK);
    C99_CHECK(wet_configure_blanking(vm, 20.0f, 1) == WET_OK);
    C99_CHECK(wet_configure_blanking(vm, 0.09f, 0) == WET_ERR_INVALID_ARG);
    C99_CHECK(wet_configure_blanking(vm, 20.1f, 0) == WET_ERR_INVALID_ARG);
    C99_CHECK(wet_configure_blanking(vm, make_nan_f(), 0) == WET_ERR_INVALID_ARG);
    C99_CHECK(wet_configure_blanking(vm, make_pos_inf_f(), 0) == WET_ERR_INVALID_ARG);
    C99_CHECK(wet_configure_blanking(vm, make_neg_inf_f(), 0) == WET_ERR_INVALID_ARG);

    C99_CHECK(wet_configure_channel_blanking(vm, 3U, 0.5f, 0U) == WET_OK);
    C99_CHECK(wet_configure_channel_blanking(vm, 0xFFFFU, 1.0f, 1U) == WET_OK);
    C99_CHECK(wet_configure_channel_blanking(vm, 64U, 1.0f, 0U) == WET_ERR_OUT_OF_BOUNDS_CH);

    /* Bytecode SET_BLANKING (0x62, <HfB, 8 bytes) valid round-trip */
    uint8_t code_ok[10];
    code_ok[0] = WET_OP_SET_BLANKING;
    write_u16_le(code_ok + 1, 0xFFFFU);
    write_f32_le(code_ok + 3, 0.3f);
    code_ok[7] = 0U;
    code_ok[8] = WET_OP_SYNC_TICK;
    code_ok[9] = WET_OP_HALT;

    uint8_t wbc[128];
    size_t wbc_len = build_wbc_stream(wbc, sizeof(wbc), WET_CAP_STIMULATION, code_ok, sizeof(code_ok));
    C99_CHECK(wbc_len > 0U);
    char err_buf[256];
    C99_CHECK(wet_verify_bytecode(wbc, wbc_len, err_buf, sizeof(err_buf)) == WET_OK);
    C99_CHECK(wet_load_bytecode(vm, wbc, wbc_len, err_buf, sizeof(err_buf)) == WET_OK);

    wet_telemetry_t telem;
    memset(&telem, 0, sizeof(telem));
    C99_CHECK(wet_step_tick(vm, &telem) == WET_OK);

    /* Bytecode SET_BLANKING invalid duration (25.0 ms > 20.0 ms) must return WET_ERR_INVALID_ARG */
    uint8_t code_bad[10];
    code_bad[0] = WET_OP_SET_BLANKING;
    write_u16_le(code_bad + 1, 0U);
    write_f32_le(code_bad + 3, 25.0f);
    code_bad[7] = 0U;
    code_bad[8] = WET_OP_SYNC_TICK;
    code_bad[9] = WET_OP_HALT;
    wbc_len = build_wbc_stream(wbc, sizeof(wbc), WET_CAP_STIMULATION, code_bad, sizeof(code_bad));
    C99_CHECK(wet_verify_bytecode(wbc, wbc_len, err_buf, sizeof(err_buf)) == WET_OK);
    C99_CHECK(wet_load_bytecode(vm, wbc, wbc_len, err_buf, sizeof(err_buf)) == WET_OK);
    C99_CHECK(wet_step_tick(vm, &telem) == WET_ERR_INVALID_ARG);

    wet_free_vm(vm);
}

static void test_closed_loop_arena_and_safety(void) {
    static uint8_t arena[512 * 1024];
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.max_stack_depth = 512;
    cfg.max_locals = 128;
    cfg.channel_count = 64;
    cfg.max_ops_per_tick = 10000;

    wet_vm_t* vm = wet_create_vm_arena(arena, sizeof(arena), &cfg);
    C99_CHECK(vm != NULL);
    C99_CHECK(wet_configure_blanking(vm, 0.1f, 0U) == WET_OK);

    hook_test_ctx_t ctx;
    memset(&ctx, 0, sizeof(ctx));
    ctx.vm = vm;
    C99_CHECK(wet_register_closed_loop_hook(vm, hook_blanking_and_1000ticks, &ctx) == WET_OK);

    uint32_t executed = 0U;
    wet_telemetry_t telem;
    memset(&telem, 0, sizeof(telem));
    C99_CHECK(wet_run_ticks(vm, 1050U, &executed, &telem) == WET_OK);
    C99_CHECK(executed == 1050U);
    C99_CHECK(ctx.calls == 1050U);
    C99_CHECK(ctx.blanked_ticks_seen == 3U);
    C99_CHECK(ctx.spikes_during_blanking == 0U);
    C99_CHECK(ctx.seen_post_stim_zero_v == 1U);
    C99_CHECK(ctx.unblanked_ticks_after == 6U);

    /* Reentrant hook clearing */
    memset(&ctx, 0, sizeof(ctx));
    ctx.vm = vm;
    C99_CHECK(wet_register_closed_loop_hook(vm, hook_reentrant_clear, &ctx) == WET_OK);
    /* Reset tick by loading empty bytecode */
    uint8_t code_sync[2] = { WET_OP_SYNC_TICK, WET_OP_HALT };
    uint8_t wbc[128];
    size_t wbc_len = build_wbc_stream(wbc, sizeof(wbc), WET_CAP_STIMULATION, code_sync, sizeof(code_sync));
    char err_buf[256];
    C99_CHECK(wet_load_bytecode(vm, wbc, wbc_len, err_buf, sizeof(err_buf)) == WET_OK);
    C99_CHECK(wet_run_ticks(vm, 10U, &executed, &telem) == WET_OK);
    C99_CHECK(ctx.reentrant_cleared == 1U);
    C99_CHECK(ctx.calls == 3U);

    wet_free_vm(vm);

    /* Safety interlock checks via closed-loop hooks */
    wet_vm_t* vm_sh = wet_create_vm(&cfg);
    C99_CHECK(vm_sh != NULL);
    C99_CHECK(wet_configure_electrode_area(vm_sh, 1U, 1e-4f) == WET_OK);
    C99_CHECK(wet_configure_electrode_area(vm_sh, 1U, 0.0f) == WET_ERR_INVALID_ARG);
    C99_CHECK(wet_configure_electrode_area(vm_sh, 1U, make_nan_f()) == WET_ERR_INVALID_ARG);
    /* Q == 0 safe check */
    C99_CHECK(wet_inject_current_stimulus(vm_sh, 1U, 0.0f, 0.5f, 0.5f) == WET_OK);
    /* Hook violating Shannon k-limit */
    C99_CHECK(wet_register_closed_loop_hook(vm_sh, hook_shannon_violation, NULL) == WET_OK);
    C99_CHECK(wet_step_tick(vm_sh, &telem) == WET_ERR_CHARGE_DENSITY_EXCEEDED);
    C99_CHECK(wet_step_tick(vm_sh, &telem) == WET_ERR_INTERLOCK_LOCKED);
    wet_free_vm(vm_sh);

    /* Reference bank violation via hook */
    wet_vm_t* vm_ref = wet_create_vm(&cfg);
    C99_CHECK(vm_ref != NULL);
    wet_set_channel_banks(vm_ref, (1ULL << 2), 0ULL);
    C99_CHECK(wet_register_closed_loop_hook(vm_ref, hook_ref_bank_violation, NULL) == WET_OK);
    C99_CHECK(wet_step_tick(vm_ref, &telem) == WET_ERR_CAPABILITY_DENIED);
    wet_free_vm(vm_ref);

    /* Out-of-bounds channel via hook */
    wet_vm_t* vm_oob = wet_create_vm(&cfg);
    C99_CHECK(vm_oob != NULL);
    C99_CHECK(wet_register_closed_loop_hook(vm_oob, hook_oob_channel, NULL) == WET_OK);
    C99_CHECK(wet_step_tick(vm_oob, &telem) == WET_ERR_OUT_OF_BOUNDS_CH);
    wet_free_vm(vm_oob);
}

static void test_determinism_and_large_bytecode(void) {
    wet_vm_config_t cfg;
    memset(&cfg, 0, sizeof(cfg));
    cfg.dt_ms = 0.1;
    cfg.max_stack_depth = 256;
    cfg.max_locals = 64;
    cfg.channel_count = 64;
    cfg.max_ops_per_tick = 10000;

    wet_vm_t* vm1 = wet_create_vm(&cfg);
    wet_vm_t* vm2 = wet_create_vm(&cfg);
    C99_CHECK(vm1 != NULL && vm2 != NULL);

    C99_CHECK(wet_vm_set_noise_enabled(vm1, 0U) == WET_OK);
    C99_CHECK(wet_vm_set_noise_enabled(vm2, 0U) == WET_OK);
    C99_CHECK(wet_vm_set_rng_seed(vm1, 424242ULL) == WET_OK);
    C99_CHECK(wet_vm_set_rng_seed(vm2, 424242ULL) == WET_OK);

    wet_telemetry_t t1, t2;
    memset(&t1, 0, sizeof(t1));
    memset(&t2, 0, sizeof(t2));
    for (int k = 0; k < 200; ++k) {
        C99_CHECK(wet_step_tick(vm1, &t1) == WET_OK);
        C99_CHECK(wet_step_tick(vm2, &t2) == WET_OK);
        C99_CHECK(memcmp(t1.voltages, t2.voltages, sizeof(t1.voltages)) == 0);
        C99_CHECK(memcmp(t1.spikes, t2.spikes, sizeof(t1.spikes)) == 0);
        for (int ch = 0; ch < 64; ++ch) {
            C99_CHECK(t1.spikes[ch] == 0U);
        }
    }

    wet_free_vm(vm1);
    wet_free_vm(vm2);

    /* Large bytecode (> 16384 bytes) to verify stack-bitset + decode-walk fallback without malloc */
    size_t code_len = 17000U;
    size_t wbc_cap = WET_HEADER_SIZE + WET_SECTION_ENTRY_SIZE + code_len;
    uint8_t* wbc = (uint8_t*)malloc(wbc_cap);
    uint8_t* code = (uint8_t*)malloc(code_len);
    C99_CHECK(wbc != NULL && code != NULL);
    if (wbc && code) {
        memset(code, WET_OP_NOP, code_len);
        /* At offset 16990, JMP +6 -> target 16996 (>= 16384), where HALT sits */
        code[16990] = WET_OP_JMP;
        code[16991] = 6U;
        code[16992] = 0U;
        code[16996] = WET_OP_HALT;
        size_t total = build_wbc_stream(wbc, wbc_cap, WET_CAP_NONE, code, code_len);
        char err_buf[256];
        C99_CHECK(wet_verify_bytecode(wbc, total, err_buf, sizeof(err_buf)) == WET_OK);

        /* Misaligned jump target >= 16384 (landing inside a 3-byte JMP at 16990) must fail */
        code[16987] = WET_OP_JMP;
        code[16988] = 4U; /* 16987 + 4 = 16991 (middle of JMP at 16990) */
        code[16989] = 0U;
        total = build_wbc_stream(wbc, wbc_cap, WET_CAP_NONE, code, code_len);
        C99_CHECK(wet_verify_bytecode(wbc, total, err_buf, sizeof(err_buf)) == WET_ERR_BYTECODE_VERIFICATION);
    }
    free(code);
    free(wbc);
}

int main(void) {
    test_blanking_api_and_bytecode();
    test_closed_loop_arena_and_safety();
    test_determinism_and_large_bytecode();

    if (g_failures == 0) {
        puts("ALL C99 CLOSED-LOOP & BLANKING TESTS PASSED");
        return 0;
    }
    printf("C99 CLOSED-LOOP TESTS FAILED: %d\n", g_failures);
    return 1;
}
