#ifndef WET_CRT_H
#define WET_CRT_H

#include <stddef.h>
#include <stdint.h>

void* malloc(size_t size);
void* calloc(size_t num, size_t size);
void  free(void* ptr);
void* memcpy(void* dest, const void* src, size_t count);
void* memset(void* dest, int ch, size_t count);
int   memcmp(const void* s1, const void* s2, size_t count);
size_t strlen(const char* str);
char* strncpy(char* dest, const char* src, size_t count);
char* strcpy(char* dest, const char* src);
char* strcat(char* dest, const char* src);
int   strcmp(const char* s1, const char* s2);
int   strncmp(const char* s1, const char* s2, size_t count);
int   sprintf(char* buffer, const char* format, ...);
int   _snprintf(char* buffer, size_t count, const char* format, ...);
#ifndef snprintf
#define snprintf _snprintf
#endif

static inline float wet_fabsf(float x) {
    return (x < 0.0f) ? -x : x;
}
#ifndef fabsf
#define fabsf wet_fabsf
#endif

static inline double wet_fabs(double x) {
    return (x < 0.0) ? -x : x;
}

static inline float wet_clampf(float x, float lo, float hi) {
    if (x < lo) return lo;
    if (x > hi) return hi;
    return x;
}

static inline double wet_clampd(double x, double lo, double hi) {
    if (x < lo) return lo;
    if (x > hi) return hi;
    return x;
}

static inline int64_t wet_llround(double x) {
    return (x >= 0.0) ? (int64_t)(x + 0.5) : (int64_t)(x - 0.5);
}

/* Pure C99 deterministic exp(x) via range reduction (Cody-Waite) + minimax polynomial.
 * Accurate to < 1e-6 for all biophysical inputs; zero external libm dependency. */
static inline double wet_exp(double x) {
    if (x < -700.0) return 0.0;
    if (x > 700.0)  return 1e300;
    const double LN2_INV = 1.44269504088896340736;
    const double LN2_HI  = 0.69314718055994530942;
    int k = (int)(x * LN2_INV + (x >= 0.0 ? 0.5 : -0.5));
    double r = x - (double)k * LN2_HI;
    /* 7th-order Taylor/Horner on [-ln2/2, ln2/2] -> error < 1e-9 */
    double poly = 1.0 + r * (1.0 + r * (0.5 + r * (1.0/6.0 + r * (1.0/24.0
                + r * (1.0/120.0 + r * (1.0/720.0 + r * (1.0/5040.0)))))));
    /* Multiply by 2^k via IEEE-754 exponent manipulation */
    union { double d; uint64_t u; } scale;
    int exp_bits = k + 1023;
    if (exp_bits <= 0) return 0.0;
    if (exp_bits >= 2047) return 1e300;
    scale.u = ((uint64_t)exp_bits) << 52;
    return poly * scale.d;
}

static inline float wet_expf(float x) {
    return (float)wet_exp((double)x);
}

/* Pure C99 Newton-Raphson sqrt(x) */
static inline double wet_sqrt(double x) {
    if (x <= 0.0) return 0.0;
    double g = x > 1.0 ? x * 0.5 : 1.0;
    for (int i = 0; i < 16; ++i) {
        g = 0.5 * (g + x / g);
    }
    return g;
}

/* Deterministic Xorshift64* PRNG for reproducible background noise & network wiring */
static inline uint64_t wet_rng_next(uint64_t* state) {
    uint64_t x = *state;
    if (x == 0) x = 0x9E3779B97F4A7C15ULL;
    x ^= x >> 12;
    x ^= x << 25;
    x ^= x >> 27;
    *state = x;
    return x * 0x2545F4914F6CDD1DULL;
}

/* Uniform double in [0, 1) */
static inline double wet_rng_uniform(uint64_t* state) {
    return (double)(wet_rng_next(state) >> 11) * (1.0 / 9007199254740992.0);
}

/* Approximate standard normal N(0,1) via Irwin-Hall (sum of 12 uniforms - 6) */
static inline double wet_rng_normal(uint64_t* state) {
    double s = 0.0;
    for (int i = 0; i < 12; ++i) {
        s += wet_rng_uniform(state);
    }
    return s - 6.0;
}

/* Calibrated processor instruction pipeline pause */
static inline void wet_cpu_pause(void) {
#if defined(__clang__) || defined(__GNUC__)
    #if defined(__x86_64__) || defined(_M_X64) || defined(__i386__) || defined(_M_IX86)
        __builtin_ia32_pause();
    #elif defined(__aarch64__)
        __asm__ __volatile__("isb\n");
    #endif
#elif defined(_MSC_VER)
    #if defined(_M_X64) || defined(_M_IX86)
        _mm_pause();
    #endif
#endif
}

/* Atomic Acquire/Release Memory Barriers for Lock-Free Ring Buffers */
static inline uint32_t wet_atomic_load_u32_acquire(const volatile uint32_t* ptr) {
#if defined(__GNUC__) || defined(__clang__)
    return __atomic_load_n(ptr, __ATOMIC_ACQUIRE);
#else
    return *ptr;
#endif
}

static inline void wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val) {
#if defined(__GNUC__) || defined(__clang__)
    __atomic_store_n(ptr, val, __ATOMIC_RELEASE);
#else
    *ptr = val;
#endif
}

static inline uint64_t wet_atomic_load_u64_acquire(const volatile uint64_t* ptr) {
#if defined(__GNUC__) || defined(__clang__)
    return __atomic_load_n(ptr, __ATOMIC_ACQUIRE);
#else
    return *ptr;
#endif
}

static inline void wet_atomic_store_u64_release(volatile uint64_t* ptr, uint64_t val) {
#if defined(__GNUC__) || defined(__clang__)
    __atomic_store_n(ptr, val, __ATOMIC_RELEASE);
#else
    *ptr = val;
#endif
}

#endif /* WET_CRT_H */
