#if !defined(_WIN32)
#ifndef _POSIX_C_SOURCE
#define _POSIX_C_SOURCE 200809L
#endif
#if defined(__APPLE__) && !defined(_DARWIN_C_SOURCE)
#define _DARWIN_C_SOURCE
#endif
#endif

#ifndef WET_BUILDING_DLL
#define WET_BUILDING_DLL
#endif

#include "../include/wet_crt.h"
#include "../include/wet_hal_transport.h"

/* =========================================================================
 * Internal String / Formatting Helpers (Zero-Malloc)
 * ========================================================================= */

static void wet_copy_bounded(char* dst, size_t dst_cap, const char* src) {
    if (!dst || dst_cap == 0U) return;
    if (!src) {
        dst[0] = '\0';
        return;
    }
    size_t i = 0U;
    while (i + 1U < dst_cap && src[i] != '\0') {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
}

static void wet_fmt_u16(uint16_t val, char* buf, size_t cap) {
    if (!buf || cap == 0U) return;
    char tmp[8];
    size_t n = 0U;
    unsigned int v = (unsigned int)val;
    if (v == 0U) {
        tmp[n++] = '0';
    } else {
        while (v > 0U && n < sizeof(tmp)) {
            tmp[n++] = (char)('0' + (v % 10U));
            v /= 10U;
        }
    }
    size_t out = 0U;
    while (n > 0U && out + 1U < cap) {
        buf[out++] = tmp[--n];
    }
    buf[out] = '\0';
}

/* =========================================================================
 * Platform Backend: Windows Direct Win32 & Winsock2 ABI (No Windows SDK)
 * ========================================================================= */

#if defined(_WIN32)

typedef void*          WET_HANDLE;
typedef unsigned long  WET_DWORD;
typedef unsigned short WET_WORD;
typedef unsigned char  WET_BYTE;
typedef int            WET_BOOL;
typedef uintptr_t      WET_SOCKET;

#define WET_INVALID_HANDLE ((WET_HANDLE)(intptr_t)-1)
#define WET_INVALID_SOCKET ((WET_SOCKET)(~(uintptr_t)0))
#define WET_SOCKET_ERROR   (-1)

#define WET_GENERIC_READ          0x80000000UL
#define WET_GENERIC_WRITE         0x40000000UL
#define WET_OPEN_EXISTING         3UL
#define WET_FILE_ATTRIBUTE_NORMAL 0x00000080UL
#define WET_FILE_TYPE_PIPE        0x0003UL

#define WET_PURGE_TXABORT         0x0001UL
#define WET_PURGE_RXABORT         0x0002UL
#define WET_PURGE_TXCLEAR         0x0004UL
#define WET_PURGE_RXCLEAR         0x0008UL

#define WET_ERROR_BROKEN_PIPE        109UL
#define WET_ERROR_PIPE_BUSY          231UL
#define WET_ERROR_NO_DATA            232UL
#define WET_ERROR_PIPE_NOT_CONNECTED 233UL

#define WET_AF_UNSPEC      0
#define WET_AF_INET        2
#define WET_SOCK_STREAM    1
#define WET_IPPROTO_TCP    6
#define WET_SOL_SOCKET     0xFFFF
#define WET_SO_ERROR       0x1007
#define WET_TCP_NODELAY    0x0001
#define WET_FIONBIO        ((long)0x8004667EUL)

#define WET_WSAEINTR       10004
#define WET_WSAEWOULDBLOCK 10035
#define WET_WSAEINPROGRESS 10036

typedef struct {
    WET_DWORD DCBlength;
    WET_DWORD BaudRate;
    WET_DWORD Flags;
    WET_WORD  wReserved;
    WET_WORD  XonLim;
    WET_WORD  XoffLim;
    WET_BYTE  ByteSize;
    WET_BYTE  Parity;
    WET_BYTE  StopBits;
    char      XonChar;
    char      XoffChar;
    char      ErrorChar;
    char      EofChar;
    char      EvtChar;
    WET_WORD  wReserved1;
} WET_DCB;

typedef struct {
    WET_DWORD ReadIntervalTimeout;
    WET_DWORD ReadTotalTimeoutMultiplier;
    WET_DWORD ReadTotalTimeoutConstant;
    WET_DWORD WriteTotalTimeoutMultiplier;
    WET_DWORD WriteTotalTimeoutConstant;
} WET_COMMTIMEOUTS;

typedef struct {
    WET_DWORD Flags;
    WET_DWORD cbInQue;
    WET_DWORD cbOutQue;
} WET_COMSTAT;

typedef struct {
    WET_WORD wVersion;
    WET_WORD wHighVersion;
#ifdef _WIN64
    unsigned short iMaxSockets;
    unsigned short iMaxUdpDg;
    char*          lpVendorInfo;
    char           szDescription[257];
    char           szSystemStatus[129];
#else
    char           szDescription[257];
    char           szSystemStatus[129];
    unsigned short iMaxSockets;
    unsigned short iMaxUdpDg;
    char*          lpVendorInfo;
#endif
} WET_WSADATA;

typedef struct {
    unsigned short sa_family;
    char           sa_data[14];
} WET_SOCKADDR;

typedef struct {
    unsigned int fd_count;
    WET_SOCKET   fd_array[64];
} WET_FD_SET;

typedef struct {
    long tv_sec;
    long tv_usec;
} WET_TIMEVAL;

typedef struct WET_ADDRINFOA_S {
    int                     ai_flags;
    int                     ai_family;
    int                     ai_socktype;
    int                     ai_protocol;
    size_t                  ai_addrlen;
    char*                   ai_canonname;
    WET_SOCKADDR*           ai_addr;
    struct WET_ADDRINFOA_S* ai_next;
} WET_ADDRINFOA;

#ifdef __cplusplus
extern "C" {
#endif
WET_HANDLE __stdcall CreateFileA(const char* lpFileName, WET_DWORD dwDesiredAccess, WET_DWORD dwShareMode, void* lpSecurityAttributes, WET_DWORD dwCreationDisposition, WET_DWORD dwFlagsAndAttributes, WET_HANDLE hTemplateFile);
WET_BOOL   __stdcall CloseHandle(WET_HANDLE hObject);
WET_DWORD  __stdcall GetFileType(WET_HANDLE hFile);
WET_BOOL   __stdcall GetCommState(WET_HANDLE hFile, WET_DCB* lpDCB);
WET_BOOL   __stdcall SetCommState(WET_HANDLE hFile, WET_DCB* lpDCB);
WET_BOOL   __stdcall GetCommTimeouts(WET_HANDLE hFile, WET_COMMTIMEOUTS* lpCommTimeouts);
WET_BOOL   __stdcall SetCommTimeouts(WET_HANDLE hFile, WET_COMMTIMEOUTS* lpCommTimeouts);
WET_BOOL   __stdcall PurgeComm(WET_HANDLE hFile, WET_DWORD dwFlags);
WET_BOOL   __stdcall ClearCommError(WET_HANDLE hFile, WET_DWORD* lpErrors, WET_COMSTAT* lpStat);
WET_BOOL   __stdcall ReadFile(WET_HANDLE hFile, void* lpBuffer, WET_DWORD nNumberOfBytesToRead, WET_DWORD* lpNumberOfBytesRead, void* lpOverlapped);
WET_BOOL   __stdcall WriteFile(WET_HANDLE hFile, const void* lpBuffer, WET_DWORD nNumberOfBytesToWrite, WET_DWORD* lpNumberOfBytesWritten, void* lpOverlapped);
WET_BOOL   __stdcall PeekNamedPipe(WET_HANDLE hNamedPipe, void* lpBuffer, WET_DWORD nBufferSize, WET_DWORD* lpBytesRead, WET_DWORD* lpTotalBytesAvail, WET_DWORD* lpBytesLeftThisMessage);
WET_BOOL   __stdcall WaitNamedPipeA(const char* lpNamedPipeName, WET_DWORD nTimeOut);
WET_DWORD  __stdcall GetLastError(void);
void       __stdcall Sleep(WET_DWORD dwMilliseconds);

int        __stdcall WSAStartup(WET_WORD wVersionRequested, WET_WSADATA* lpWSAData);
int        __stdcall WSACleanup(void);
int        __stdcall WSAGetLastError(void);
WET_SOCKET __stdcall socket(int af, int type, int protocol);
int        __stdcall closesocket(WET_SOCKET s);
int        __stdcall connect(WET_SOCKET s, const WET_SOCKADDR* name, int namelen);
int        __stdcall send(WET_SOCKET s, const char* buf, int len, int flags);
int        __stdcall recv(WET_SOCKET s, char* buf, int len, int flags);
int        __stdcall ioctlsocket(WET_SOCKET s, long cmd, unsigned long* argp);
int        __stdcall select(int nfds, WET_FD_SET* readfds, WET_FD_SET* writefds, WET_FD_SET* exceptfds, const WET_TIMEVAL* timeout);
int        __stdcall setsockopt(WET_SOCKET s, int level, int optname, const char* optval, int optlen);
int        __stdcall getsockopt(WET_SOCKET s, int level, int optname, char* optval, int* optlen);
int        __stdcall getaddrinfo(const char* pNodeName, const char* pServiceName, const WET_ADDRINFOA* pHints, WET_ADDRINFOA** ppResult);
void       __stdcall freeaddrinfo(WET_ADDRINFOA* pAddrInfo);
#ifdef __cplusplus
}
#endif

#if defined(_MSC_VER) && !defined(__clang__)
long _InterlockedCompareExchange(long volatile*, long, long);
#pragma intrinsic(_InterlockedCompareExchange)
#endif

static inline int wet_transport_cas_u32(volatile uint32_t* ptr, uint32_t expected, uint32_t desired) {
#if defined(__GNUC__) || defined(__clang__)
    return __atomic_compare_exchange_n(ptr, &expected, desired, 0, __ATOMIC_ACQ_REL, __ATOMIC_ACQUIRE);
#elif defined(_MSC_VER)
    return (_InterlockedCompareExchange((volatile long*)ptr, (long)desired, (long)expected) == (long)expected);
#else
    if (*ptr == expected) { *ptr = desired; return 1; }
    return 0;
#endif
}

static volatile uint32_t g_wsa_lock = 0U;
static uint32_t g_wsa_refcount = 0U;

static void wet_wsa_lock(void) {
    while (!wet_transport_cas_u32(&g_wsa_lock, 0U, 1U)) {
        wet_cpu_pause();
    }
}

static void wet_wsa_unlock(void) {
    wet_atomic_store_u32_release(&g_wsa_lock, 0U);
}

static int wet_wsa_acquire(void) {
    wet_wsa_lock();
    if (g_wsa_refcount == 0U) {
        WET_WSADATA wsa;
        memset(&wsa, 0, sizeof(wsa));
        if (WSAStartup(0x0202U, &wsa) != 0) {
            wet_wsa_unlock();
            return 0;
        }
    }
    g_wsa_refcount++;
    wet_wsa_unlock();
    return 1;
}

static void wet_wsa_release(void) {
    wet_wsa_lock();
    if (g_wsa_refcount > 0U) {
        g_wsa_refcount--;
        if (g_wsa_refcount == 0U) {
            WSACleanup();
        }
    }
    wet_wsa_unlock();
}

static char wet_ascii_upper(char c) {
    if (c >= 'a' && c <= 'z') return (char)(c - 'a' + 'A');
    return c;
}

wet_hal_status_t wet_hal_transport_normalize_port(
    const char* port_name,
    char* out_buf,
    size_t buf_cap
) {
    if (!port_name || !out_buf) return WET_HAL_ERR_NULL_PTR;
    if (buf_cap == 0U) return WET_HAL_ERR_BUFFER_FULL;
    size_t len = strlen(port_name);
    if (len == 0U) return WET_HAL_ERR_OUT_OF_BOUNDS;

    if ((len >= 4U && memcmp(port_name, "\\\\.\\", 4U) == 0) ||
        (len >= 4U && memcmp(port_name, "\\\\?\\", 4U) == 0) ||
        (len >= 4U && memcmp(port_name, "//./", 4U) == 0)) {
        if (len + 1U > buf_cap) return WET_HAL_ERR_BUFFER_FULL;
        memcpy(out_buf, port_name, len + 1U);
        return WET_HAL_OK;
    }

    if (len >= 4U &&
        wet_ascii_upper(port_name[0]) == 'C' &&
        wet_ascii_upper(port_name[1]) == 'O' &&
        wet_ascii_upper(port_name[2]) == 'M') {
        size_t pos = 3U;
        uint32_t com_num = 0U;
        int all_digits = 1;
        while (pos < len) {
            char ch = port_name[pos];
            if (ch < '0' || ch > '9') {
                all_digits = 0;
                break;
            }
            if (com_num < 100000U) {
                com_num = com_num * 10U + (uint32_t)(ch - '0');
            }
            pos++;
        }
        if (all_digits) {
            size_t digit_len = len - 3U;
            if (com_num >= 10U) {
                /* Format "\\.\COM" + digits */
                if (7U + digit_len + 1U > buf_cap) return WET_HAL_ERR_BUFFER_FULL;
                memcpy(out_buf, "\\\\.\\COM", 7U);
                memcpy(out_buf + 7U, port_name + 3U, digit_len + 1U);
                return WET_HAL_OK;
            } else {
                if (3U + digit_len + 1U > buf_cap) return WET_HAL_ERR_BUFFER_FULL;
                memcpy(out_buf, "COM", 3U);
                memcpy(out_buf + 3U, port_name + 3U, digit_len + 1U);
                return WET_HAL_OK;
            }
        }
    }

    if (len + 1U > buf_cap) return WET_HAL_ERR_BUFFER_FULL;
    memcpy(out_buf, port_name, len + 1U);
    return WET_HAL_OK;
}

void wet_hal_serial_init(wet_hal_serial_t* ser) {
    if (!ser) return;
    memset(ser, 0, sizeof(*ser));
    ser->os_handle = (uintptr_t)WET_INVALID_HANDLE;
    ser->fd = -1;
}

wet_hal_status_t wet_hal_serial_open(
    wet_hal_serial_t* ser,
    const char* port_name,
    uint32_t baud_rate,
    uint32_t timeout_ms
) {
    if (!ser || !port_name) return WET_HAL_ERR_NULL_PTR;
    if (ser->is_open) {
        wet_hal_serial_close(ser);
    }
    wet_hal_serial_init(ser);

    char norm_path[WET_HAL_TRANSPORT_MAX_PATH];
    wet_hal_status_t norm_st = wet_hal_transport_normalize_port(port_name, norm_path, sizeof(norm_path));
    if (norm_st != WET_HAL_OK) return norm_st;

    uint32_t eff_timeout = (timeout_ms > 0U) ? timeout_ms : 1000U;
    uint32_t eff_baud = (baud_rate > 0U) ? baud_rate : 115200U;

    WET_HANDLE h = CreateFileA(
        norm_path,
        WET_GENERIC_READ | WET_GENERIC_WRITE,
        0UL,
        NULL,
        WET_OPEN_EXISTING,
        WET_FILE_ATTRIBUTE_NORMAL,
        NULL
    );
    if (h == WET_INVALID_HANDLE && GetLastError() == WET_ERROR_PIPE_BUSY) {
        WaitNamedPipeA(norm_path, (WET_DWORD)eff_timeout);
        h = CreateFileA(
            norm_path,
            WET_GENERIC_READ | WET_GENERIC_WRITE,
            0UL,
            NULL,
            WET_OPEN_EXISTING,
            WET_FILE_ATTRIBUTE_NORMAL,
            NULL
        );
    }
    if (h == WET_INVALID_HANDLE) {
        return WET_HAL_ERR_IO;
    }

    WET_DWORD ftype = GetFileType(h);
    if (ftype == WET_FILE_TYPE_PIPE) {
        ser->is_pipe = 1U;
    } else {
        WET_DCB dcb;
        memset(&dcb, 0, sizeof(dcb));
        dcb.DCBlength = (WET_DWORD)sizeof(WET_DCB);
        if (!GetCommState(h, &dcb)) {
            CloseHandle(h);
            return WET_HAL_ERR_IO;
        }
        dcb.BaudRate = (WET_DWORD)eff_baud;
        dcb.Flags = 0x00000001UL; /* fBinary = 1, raw 8N1 without flow control */
        dcb.ByteSize = 8;
        dcb.Parity = 0;
        dcb.StopBits = 0;
        if (!SetCommState(h, &dcb)) {
            CloseHandle(h);
            return WET_HAL_ERR_IO;
        }

        WET_COMMTIMEOUTS cto;
        memset(&cto, 0, sizeof(cto));
        cto.ReadIntervalTimeout = 0xFFFFFFFFUL;
        cto.ReadTotalTimeoutMultiplier = 0xFFFFFFFFUL;
        cto.ReadTotalTimeoutConstant = (WET_DWORD)eff_timeout;
        cto.WriteTotalTimeoutMultiplier = 0UL;
        cto.WriteTotalTimeoutConstant = (WET_DWORD)eff_timeout;
        if (!SetCommTimeouts(h, &cto)) {
            CloseHandle(h);
            return WET_HAL_ERR_IO;
        }
        PurgeComm(h, WET_PURGE_RXCLEAR | WET_PURGE_TXCLEAR);
        ser->is_pipe = 0U;
    }

    ser->os_handle = (uintptr_t)h;
    ser->fd = -1;
    ser->baud_rate = eff_baud;
    ser->timeout_ms = eff_timeout;
    ser->is_open = 1U;
    wet_copy_bounded(ser->port_name, sizeof(ser->port_name), norm_path);
    return WET_HAL_OK;
}

void wet_hal_serial_close(wet_hal_serial_t* ser) {
    if (!ser) return;
    if (ser->is_open && ser->os_handle != (uintptr_t)WET_INVALID_HANDLE) {
        CloseHandle((WET_HANDLE)ser->os_handle);
    }
    wet_hal_serial_init(ser);
}

int wet_hal_serial_is_open(const wet_hal_serial_t* ser) {
    if (!ser) return 0;
    return (ser->is_open != 0U && ser->os_handle != (uintptr_t)WET_INVALID_HANDLE) ? 1 : 0;
}

wet_hal_status_t wet_hal_serial_write(
    wet_hal_serial_t* ser,
    const void* data,
    size_t len,
    size_t* out_written
) {
    if (out_written) *out_written = 0U;
    if (!ser || (!data && len > 0U)) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;
    if (len == 0U) return WET_HAL_OK;

    WET_HANDLE h = (WET_HANDLE)ser->os_handle;
    const uint8_t* ptr = (const uint8_t*)data;
    size_t total = 0U;
    while (total < len) {
        size_t rem = len - total;
        WET_DWORD chunk = (rem > 65536U) ? 65536UL : (WET_DWORD)rem;
        WET_DWORD wrote = 0UL;
        if (!WriteFile(h, ptr + total, chunk, &wrote, NULL) || wrote == 0UL) {
            if (out_written) *out_written = total;
            return WET_HAL_ERR_IO;
        }
        total += (size_t)wrote;
    }
    if (out_written) *out_written = total;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_serial_read(
    wet_hal_serial_t* ser,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
) {
    if (out_read) *out_read = 0U;
    if (!ser || !buf) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;
    if (max_len == 0U) return WET_HAL_OK;

    WET_HANDLE h = (WET_HANDLE)ser->os_handle;

    if (ser->is_pipe) {
        uint64_t start_us = wet_hal_get_time_us();
        uint64_t deadline_us = start_us + (uint64_t)timeout_ms * 1000ULL;
        for (;;) {
            WET_DWORD avail = 0UL;
            if (!PeekNamedPipe(h, NULL, 0UL, NULL, &avail, NULL)) {
                return WET_HAL_ERR_IO;
            }
            if (avail > 0UL) {
                WET_DWORD to_read = ((size_t)avail < max_len) ? avail : (WET_DWORD)max_len;
                WET_DWORD got = 0UL;
                if (!ReadFile(h, buf, to_read, &got, NULL) || got == 0UL) {
                    return WET_HAL_ERR_IO;
                }
                if (out_read) *out_read = (size_t)got;
                return WET_HAL_OK;
            }
            if (timeout_ms == 0U || wet_hal_get_time_us() >= deadline_us) {
                return WET_HAL_ERR_TIMEOUT;
            }
            Sleep(1UL);
        }
    } else {
        if (timeout_ms != ser->timeout_ms) {
            WET_COMMTIMEOUTS cto;
            memset(&cto, 0, sizeof(cto));
            cto.ReadIntervalTimeout = 0xFFFFFFFFUL;
            cto.ReadTotalTimeoutMultiplier = (timeout_ms == 0U) ? 0UL : 0xFFFFFFFFUL;
            cto.ReadTotalTimeoutConstant = (WET_DWORD)timeout_ms;
            cto.WriteTotalTimeoutMultiplier = 0UL;
            cto.WriteTotalTimeoutConstant = (WET_DWORD)(ser->timeout_ms > 0U ? ser->timeout_ms : 1000U);
            if (!SetCommTimeouts(h, &cto)) {
                return WET_HAL_ERR_IO;
            }
            ser->timeout_ms = timeout_ms;
        }
        WET_DWORD to_read = (max_len > 65536U) ? 65536UL : (WET_DWORD)max_len;
        WET_DWORD got = 0UL;
        if (!ReadFile(h, buf, to_read, &got, NULL)) {
            return WET_HAL_ERR_IO;
        }
        if (got == 0UL) {
            return WET_HAL_ERR_TIMEOUT;
        }
        if (out_read) *out_read = (size_t)got;
        return WET_HAL_OK;
    }
}

void wet_hal_tcp_init(wet_hal_tcp_t* tcp) {
    if (!tcp) return;
    memset(tcp, 0, sizeof(*tcp));
    tcp->sock = (uintptr_t)WET_INVALID_SOCKET;
}

static wet_hal_status_t wet_win32_select_socket(
    WET_SOCKET s,
    int wait_read,
    int wait_write,
    uint32_t timeout_ms
) {
    WET_FD_SET rfds;
    WET_FD_SET wfds;
    WET_FD_SET efds;
    WET_TIMEVAL tv;

    rfds.fd_count = 1U;
    rfds.fd_array[0] = s;
    wfds.fd_count = 1U;
    wfds.fd_array[0] = s;
    efds.fd_count = 1U;
    efds.fd_array[0] = s;

    tv.tv_sec = (long)(timeout_ms / 1000U);
    tv.tv_usec = (long)((timeout_ms % 1000U) * 1000U);

    int rc = select(
        0,
        wait_read ? &rfds : NULL,
        wait_write ? &wfds : NULL,
        &efds,
        &tv
    );
    if (rc == WET_SOCKET_ERROR) {
        return WET_HAL_ERR_IO;
    }
    if (rc == 0) {
        return WET_HAL_ERR_TIMEOUT;
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_tcp_connect(
    wet_hal_tcp_t* tcp,
    const char* host,
    uint16_t port,
    uint32_t timeout_ms
) {
    if (!tcp || !host) return WET_HAL_ERR_NULL_PTR;
    if (host[0] == '\0' || port == 0U) return WET_HAL_ERR_OUT_OF_BOUNDS;
    if (tcp->is_connected || tcp->wsa_acquired) {
        wet_hal_tcp_close(tcp);
    }
    wet_hal_tcp_init(tcp);

    if (!wet_wsa_acquire()) {
        return WET_HAL_ERR_IO;
    }
    tcp->wsa_acquired = 1U;

    uint32_t eff_timeout = (timeout_ms > 0U) ? timeout_ms : 1000U;
    char port_str[8];
    wet_fmt_u16(port, port_str, sizeof(port_str));

    WET_ADDRINFOA hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = WET_AF_UNSPEC;
    hints.ai_socktype = WET_SOCK_STREAM;
    hints.ai_protocol = WET_IPPROTO_TCP;

    WET_ADDRINFOA* res = NULL;
    if (getaddrinfo(host, port_str, &hints, &res) != 0 || res == NULL) {
        wet_wsa_release();
        tcp->wsa_acquired = 0U;
        return WET_HAL_ERR_IO;
    }

    uint64_t start_us = wet_hal_get_time_us();
    uint64_t deadline_us = start_us + (uint64_t)eff_timeout * 1000ULL;
    WET_SOCKET connected_sock = WET_INVALID_SOCKET;
    wet_hal_status_t last_err = WET_HAL_ERR_IO;

    for (WET_ADDRINFOA* rp = res; rp != NULL; rp = rp->ai_next) {
        WET_SOCKET s = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (s == WET_INVALID_SOCKET) {
            continue;
        }

        int nodelay = 1;
        setsockopt(s, WET_IPPROTO_TCP, WET_TCP_NODELAY, (const char*)&nodelay, (int)sizeof(nodelay));

        unsigned long nb = 1UL;
        if (ioctlsocket(s, WET_FIONBIO, &nb) != 0) {
            closesocket(s);
            continue;
        }

        int rc = connect(s, rp->ai_addr, (int)rp->ai_addrlen);
        if (rc == 0) {
            connected_sock = s;
            break;
        }

        int werr = WSAGetLastError();
        if (werr == WET_WSAEWOULDBLOCK || werr == WET_WSAEINPROGRESS) {
            for (;;) {
                uint64_t now_us = wet_hal_get_time_us();
                if (now_us >= deadline_us) {
                    closesocket(s);
                    last_err = WET_HAL_ERR_TIMEOUT;
                    break;
                }
                uint32_t rem_ms = (uint32_t)((deadline_us - now_us + 999ULL) / 1000ULL);
                if (rem_ms == 0U) rem_ms = 1U;
                wet_hal_status_t sst = wet_win32_select_socket(s, 0, 1, rem_ms);
                if (sst == WET_HAL_ERR_TIMEOUT) {
                    closesocket(s);
                    last_err = WET_HAL_ERR_TIMEOUT;
                    break;
                }
                if (sst != WET_HAL_OK) {
                    if (WSAGetLastError() == WET_WSAEINTR) continue;
                    closesocket(s);
                    last_err = WET_HAL_ERR_IO;
                    break;
                }
                int so_err = 0;
                int optlen = (int)sizeof(so_err);
                if (getsockopt(s, WET_SOL_SOCKET, WET_SO_ERROR, (char*)&so_err, &optlen) != 0 || so_err != 0) {
                    closesocket(s);
                    last_err = WET_HAL_ERR_IO;
                    break;
                }
                connected_sock = s;
                break;
            }
            if (connected_sock != WET_INVALID_SOCKET) {
                break;
            }
        } else {
            closesocket(s);
            last_err = WET_HAL_ERR_IO;
        }
    }

    freeaddrinfo(res);

    if (connected_sock == WET_INVALID_SOCKET) {
        wet_wsa_release();
        tcp->wsa_acquired = 0U;
        return last_err;
    }

    tcp->sock = (uintptr_t)connected_sock;
    tcp->timeout_ms = eff_timeout;
    tcp->port = port;
    tcp->is_connected = 1U;
    wet_copy_bounded(tcp->host, sizeof(tcp->host), host);
    return WET_HAL_OK;
}

void wet_hal_tcp_close(wet_hal_tcp_t* tcp) {
    if (!tcp) return;
    if (tcp->sock != (uintptr_t)WET_INVALID_SOCKET) {
        closesocket((WET_SOCKET)tcp->sock);
    }
    if (tcp->wsa_acquired) {
        wet_wsa_release();
    }
    wet_hal_tcp_init(tcp);
}

int wet_hal_tcp_is_connected(const wet_hal_tcp_t* tcp) {
    if (!tcp) return 0;
    return (tcp->is_connected != 0U && tcp->sock != (uintptr_t)WET_INVALID_SOCKET) ? 1 : 0;
}

wet_hal_status_t wet_hal_tcp_send_all(
    wet_hal_tcp_t* tcp,
    const void* data,
    size_t len,
    uint32_t timeout_ms,
    size_t* out_sent
) {
    if (out_sent) *out_sent = 0U;
    if (!tcp || (!data && len > 0U)) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_tcp_is_connected(tcp)) return WET_HAL_ERR_IO;
    if (len == 0U) return WET_HAL_OK;

    WET_SOCKET s = (WET_SOCKET)tcp->sock;
    const char* ptr = (const char*)data;
    size_t total = 0U;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;

    while (total < len) {
        size_t rem = len - total;
        int chunk = (rem > 65536U) ? 65536 : (int)rem;
        int rc = send(s, ptr + total, chunk, 0);
        if (rc > 0) {
            total += (size_t)rc;
            continue;
        }
        if (rc == 0) {
            if (out_sent) *out_sent = total;
            return WET_HAL_ERR_IO;
        }
        int werr = WSAGetLastError();
        if (werr == WET_WSAEINTR) {
            continue;
        }
        if (werr == WET_WSAEWOULDBLOCK) {
            uint64_t now_us = wet_hal_get_time_us();
            if (timeout_ms == 0U || now_us >= deadline_us) {
                if (out_sent) *out_sent = total;
                return WET_HAL_ERR_TIMEOUT;
            }
            uint32_t rem_ms = (uint32_t)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms == 0U) rem_ms = 1U;
            wet_hal_status_t sst = wet_win32_select_socket(s, 0, 1, rem_ms);
            if (sst != WET_HAL_OK) {
                if (out_sent) *out_sent = total;
                return sst;
            }
            continue;
        }
        if (out_sent) *out_sent = total;
        return WET_HAL_ERR_IO;
    }

    if (out_sent) *out_sent = total;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_tcp_recv(
    wet_hal_tcp_t* tcp,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
) {
    if (out_read) *out_read = 0U;
    if (!tcp || !buf) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_tcp_is_connected(tcp)) return WET_HAL_ERR_IO;
    if (max_len == 0U) return WET_HAL_OK;

    WET_SOCKET s = (WET_SOCKET)tcp->sock;
    int cap = (max_len > 65536U) ? 65536 : (int)max_len;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;

    for (;;) {
        int rc = recv(s, (char*)buf, cap, 0);
        if (rc > 0) {
            if (out_read) *out_read = (size_t)rc;
            return WET_HAL_OK;
        }
        if (rc == 0) {
            return WET_HAL_ERR_IO;
        }
        int werr = WSAGetLastError();
        if (werr == WET_WSAEINTR) {
            continue;
        }
        if (werr == WET_WSAEWOULDBLOCK) {
            uint64_t now_us = wet_hal_get_time_us();
            if (timeout_ms == 0U || now_us >= deadline_us) {
                return WET_HAL_ERR_TIMEOUT;
            }
            uint32_t rem_ms = (uint32_t)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms == 0U) rem_ms = 1U;
            wet_hal_status_t sst = wet_win32_select_socket(s, 1, 0, rem_ms);
            if (sst != WET_HAL_OK) {
                return sst;
            }
            continue;
        }
        return WET_HAL_ERR_IO;
    }
}

/* =========================================================================
 * Platform Backend: POSIX (Linux / macOS)
 * ========================================================================= */

#else

#include <errno.h>
#include <fcntl.h>
#include <poll.h>
#include <termios.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <netdb.h>

wet_hal_status_t wet_hal_transport_normalize_port(
    const char* port_name,
    char* out_buf,
    size_t buf_cap
) {
    if (!port_name || !out_buf) return WET_HAL_ERR_NULL_PTR;
    if (buf_cap == 0U) return WET_HAL_ERR_BUFFER_FULL;
    size_t len = strlen(port_name);
    if (len == 0U) return WET_HAL_ERR_OUT_OF_BOUNDS;
    if (len + 1U > buf_cap) return WET_HAL_ERR_BUFFER_FULL;
    memcpy(out_buf, port_name, len + 1U);
    return WET_HAL_OK;
}

void wet_hal_serial_init(wet_hal_serial_t* ser) {
    if (!ser) return;
    memset(ser, 0, sizeof(*ser));
    ser->fd = -1;
}

static int wet_posix_baud(uint32_t baud_rate, speed_t* out_speed) {
    switch (baud_rate) {
        case 9600U:   *out_speed = B9600;   return 1;
        case 19200U:  *out_speed = B19200;  return 1;
        case 38400U:  *out_speed = B38400;  return 1;
        case 57600U:  *out_speed = B57600;  return 1;
        case 115200U: *out_speed = B115200; return 1;
        default:      return 0;
    }
}

wet_hal_status_t wet_hal_serial_open(
    wet_hal_serial_t* ser,
    const char* port_name,
    uint32_t baud_rate,
    uint32_t timeout_ms
) {
    if (!ser || !port_name) return WET_HAL_ERR_NULL_PTR;
    if (ser->is_open) {
        wet_hal_serial_close(ser);
    }
    wet_hal_serial_init(ser);

    char norm_path[WET_HAL_TRANSPORT_MAX_PATH];
    wet_hal_status_t norm_st = wet_hal_transport_normalize_port(port_name, norm_path, sizeof(norm_path));
    if (norm_st != WET_HAL_OK) return norm_st;

    uint32_t eff_timeout = (timeout_ms > 0U) ? timeout_ms : 1000U;
    uint32_t eff_baud = (baud_rate > 0U) ? baud_rate : 115200U;

    speed_t spd = B115200;
    if (!wet_posix_baud(eff_baud, &spd)) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    int fd = open(norm_path, O_RDWR | O_NOCTTY | O_NONBLOCK);
    if (fd < 0) {
        return WET_HAL_ERR_IO;
    }

    if (isatty(fd)) {
        struct termios tio;
        if (tcgetattr(fd, &tio) != 0) {
            close(fd);
            return WET_HAL_ERR_IO;
        }
        tio.c_iflag &= (tcflag_t)~(IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL | IXON | IXOFF | IXANY);
        tio.c_oflag &= (tcflag_t)~OPOST;
        tio.c_lflag &= (tcflag_t)~(ECHO | ECHONL | ICANON | ISIG | IEXTEN);
        tio.c_cflag &= (tcflag_t)~(CSIZE | PARENB | CSTOPB);
#ifdef CRTSCTS
        tio.c_cflag &= (tcflag_t)~CRTSCTS;
#endif
        tio.c_cflag |= (tcflag_t)(CS8 | CLOCAL | CREAD);
        tio.c_cc[VMIN] = 0;
        tio.c_cc[VTIME] = 0;
        cfsetispeed(&tio, spd);
        cfsetospeed(&tio, spd);
        if (tcsetattr(fd, TCSANOW, &tio) != 0) {
            close(fd);
            return WET_HAL_ERR_IO;
        }
        tcflush(fd, TCIOFLUSH);
        ser->is_pipe = 0U;
    } else {
        ser->is_pipe = 1U;
    }

    ser->os_handle = 0U;
    ser->fd = (int32_t)fd;
    ser->baud_rate = eff_baud;
    ser->timeout_ms = eff_timeout;
    ser->is_open = 1U;
    wet_copy_bounded(ser->port_name, sizeof(ser->port_name), norm_path);
    return WET_HAL_OK;
}

void wet_hal_serial_close(wet_hal_serial_t* ser) {
    if (!ser) return;
    if (ser->is_open && ser->fd >= 0) {
        close((int)ser->fd);
    }
    wet_hal_serial_init(ser);
}

int wet_hal_serial_is_open(const wet_hal_serial_t* ser) {
    if (!ser) return 0;
    return (ser->is_open != 0U && ser->fd >= 0) ? 1 : 0;
}

wet_hal_status_t wet_hal_serial_write(
    wet_hal_serial_t* ser,
    const void* data,
    size_t len,
    size_t* out_written
) {
    if (out_written) *out_written = 0U;
    if (!ser || (!data && len > 0U)) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;
    if (len == 0U) return WET_HAL_OK;

    int fd = (int)ser->fd;
    const uint8_t* ptr = (const uint8_t*)data;
    size_t total = 0U;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)(ser->timeout_ms > 0U ? ser->timeout_ms : 1000U) * 1000ULL;

    while (total < len) {
        ssize_t n = write(fd, ptr + total, len - total);
        if (n > 0) {
            total += (size_t)n;
            continue;
        }
        if (n < 0 && errno == EINTR) {
            continue;
        }
        if (n < 0 && (errno == EAGAIN || errno == EWOULDBLOCK)) {
            uint64_t now_us = wet_hal_get_time_us();
            if (now_us >= deadline_us) {
                if (out_written) *out_written = total;
                return WET_HAL_ERR_TIMEOUT;
            }
            int rem_ms = (int)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms <= 0) rem_ms = 1;
            struct pollfd pfd;
            pfd.fd = fd;
            pfd.events = POLLOUT;
            pfd.revents = 0;
            int prc = poll(&pfd, 1, rem_ms);
            if (prc < 0 && errno == EINTR) continue;
            if (prc == 0) {
                if (out_written) *out_written = total;
                return WET_HAL_ERR_TIMEOUT;
            }
            if (prc < 0 || (pfd.revents & (POLLERR | POLLHUP | POLLNVAL)) != 0) {
                if (out_written) *out_written = total;
                return WET_HAL_ERR_IO;
            }
            continue;
        }
        if (out_written) *out_written = total;
        return WET_HAL_ERR_IO;
    }

    if (out_written) *out_written = total;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_serial_read(
    wet_hal_serial_t* ser,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
) {
    if (out_read) *out_read = 0U;
    if (!ser || !buf) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;
    if (max_len == 0U) return WET_HAL_OK;

    int fd = (int)ser->fd;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;

    for (;;) {
        ssize_t n = read(fd, buf, max_len);
        if (n > 0) {
            if (out_read) *out_read = (size_t)n;
            return WET_HAL_OK;
        }
        if (n == 0) {
            return WET_HAL_ERR_IO;
        }
        if (errno == EINTR) {
            continue;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            uint64_t now_us = wet_hal_get_time_us();
            if (timeout_ms == 0U || now_us >= deadline_us) {
                return WET_HAL_ERR_TIMEOUT;
            }
            int rem_ms = (int)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms <= 0) rem_ms = 1;
            struct pollfd pfd;
            pfd.fd = fd;
            pfd.events = POLLIN;
            pfd.revents = 0;
            int prc = poll(&pfd, 1, rem_ms);
            if (prc < 0 && errno == EINTR) continue;
            if (prc == 0) return WET_HAL_ERR_TIMEOUT;
            if (prc < 0) return WET_HAL_ERR_IO;
            if ((pfd.revents & POLLIN) == 0 && (pfd.revents & (POLLERR | POLLHUP | POLLNVAL)) != 0) {
                return WET_HAL_ERR_IO;
            }
            continue;
        }
        return WET_HAL_ERR_IO;
    }
}

void wet_hal_tcp_init(wet_hal_tcp_t* tcp) {
    if (!tcp) return;
    memset(tcp, 0, sizeof(*tcp));
    tcp->sock = (uintptr_t)(-1);
}

wet_hal_status_t wet_hal_tcp_connect(
    wet_hal_tcp_t* tcp,
    const char* host,
    uint16_t port,
    uint32_t timeout_ms
) {
    if (!tcp || !host) return WET_HAL_ERR_NULL_PTR;
    if (host[0] == '\0' || port == 0U) return WET_HAL_ERR_OUT_OF_BOUNDS;
    if (tcp->is_connected) {
        wet_hal_tcp_close(tcp);
    }
    wet_hal_tcp_init(tcp);

    uint32_t eff_timeout = (timeout_ms > 0U) ? timeout_ms : 1000U;
    char port_str[8];
    wet_fmt_u16(port, port_str, sizeof(port_str));

    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;

    struct addrinfo* res = NULL;
    if (getaddrinfo(host, port_str, &hints, &res) != 0 || res == NULL) {
        return WET_HAL_ERR_IO;
    }

    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)eff_timeout * 1000ULL;
    int connected_fd = -1;
    wet_hal_status_t last_err = WET_HAL_ERR_IO;

    for (struct addrinfo* rp = res; rp != NULL; rp = rp->ai_next) {
        int fd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (fd < 0) continue;

#ifdef SO_NOSIGPIPE
        {
            int one = 1;
            setsockopt(fd, SOL_SOCKET, SO_NOSIGPIPE, &one, (socklen_t)sizeof(one));
        }
#endif
        {
            int nodelay = 1;
            setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &nodelay, (socklen_t)sizeof(nodelay));
        }
        int flags = fcntl(fd, F_GETFL, 0);
        if (flags < 0 || fcntl(fd, F_SETFL, flags | O_NONBLOCK) < 0) {
            close(fd);
            continue;
        }

        int rc = connect(fd, rp->ai_addr, rp->ai_addrlen);
        if (rc == 0) {
            connected_fd = fd;
            break;
        }
        if (errno == EINPROGRESS) {
            for (;;) {
                uint64_t now_us = wet_hal_get_time_us();
                if (now_us >= deadline_us) {
                    close(fd);
                    last_err = WET_HAL_ERR_TIMEOUT;
                    break;
                }
                int rem_ms = (int)((deadline_us - now_us + 999ULL) / 1000ULL);
                if (rem_ms <= 0) rem_ms = 1;
                struct pollfd pfd;
                pfd.fd = fd;
                pfd.events = POLLOUT;
                pfd.revents = 0;
                int prc = poll(&pfd, 1, rem_ms);
                if (prc < 0 && errno == EINTR) continue;
                if (prc == 0) {
                    close(fd);
                    last_err = WET_HAL_ERR_TIMEOUT;
                    break;
                }
                if (prc < 0) {
                    close(fd);
                    last_err = WET_HAL_ERR_IO;
                    break;
                }
                int so_err = 0;
                socklen_t optlen = (socklen_t)sizeof(so_err);
                if (getsockopt(fd, SOL_SOCKET, SO_ERROR, &so_err, &optlen) != 0 || so_err != 0) {
                    close(fd);
                    last_err = WET_HAL_ERR_IO;
                    break;
                }
                connected_fd = fd;
                break;
            }
            if (connected_fd >= 0) break;
        } else {
            close(fd);
            last_err = WET_HAL_ERR_IO;
        }
    }

    freeaddrinfo(res);

    if (connected_fd < 0) {
        return last_err;
    }

    tcp->sock = (uintptr_t)connected_fd;
    tcp->timeout_ms = eff_timeout;
    tcp->port = port;
    tcp->is_connected = 1U;
    wet_copy_bounded(tcp->host, sizeof(tcp->host), host);
    return WET_HAL_OK;
}

void wet_hal_tcp_close(wet_hal_tcp_t* tcp) {
    if (!tcp) return;
    if (tcp->is_connected && tcp->sock != (uintptr_t)(-1)) {
        close((int)tcp->sock);
    }
    wet_hal_tcp_init(tcp);
}

int wet_hal_tcp_is_connected(const wet_hal_tcp_t* tcp) {
    if (!tcp) return 0;
    return (tcp->is_connected != 0U && tcp->sock != (uintptr_t)(-1)) ? 1 : 0;
}

wet_hal_status_t wet_hal_tcp_send_all(
    wet_hal_tcp_t* tcp,
    const void* data,
    size_t len,
    uint32_t timeout_ms,
    size_t* out_sent
) {
    if (out_sent) *out_sent = 0U;
    if (!tcp || (!data && len > 0U)) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_tcp_is_connected(tcp)) return WET_HAL_ERR_IO;
    if (len == 0U) return WET_HAL_OK;

    int fd = (int)tcp->sock;
    const uint8_t* ptr = (const uint8_t*)data;
    size_t total = 0U;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;
#ifdef MSG_NOSIGNAL
    const int sflags = MSG_NOSIGNAL;
#else
    const int sflags = 0;
#endif

    while (total < len) {
        ssize_t n = send(fd, ptr + total, len - total, sflags);
        if (n > 0) {
            total += (size_t)n;
            continue;
        }
        if (n < 0 && errno == EINTR) {
            continue;
        }
        if (n < 0 && (errno == EAGAIN || errno == EWOULDBLOCK)) {
            uint64_t now_us = wet_hal_get_time_us();
            if (timeout_ms == 0U || now_us >= deadline_us) {
                if (out_sent) *out_sent = total;
                return WET_HAL_ERR_TIMEOUT;
            }
            int rem_ms = (int)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms <= 0) rem_ms = 1;
            struct pollfd pfd;
            pfd.fd = fd;
            pfd.events = POLLOUT;
            pfd.revents = 0;
            int prc = poll(&pfd, 1, rem_ms);
            if (prc < 0 && errno == EINTR) continue;
            if (prc == 0) {
                if (out_sent) *out_sent = total;
                return WET_HAL_ERR_TIMEOUT;
            }
            if (prc < 0 || (pfd.revents & (POLLERR | POLLHUP | POLLNVAL)) != 0) {
                if (out_sent) *out_sent = total;
                return WET_HAL_ERR_IO;
            }
            continue;
        }
        if (out_sent) *out_sent = total;
        return WET_HAL_ERR_IO;
    }

    if (out_sent) *out_sent = total;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_tcp_recv(
    wet_hal_tcp_t* tcp,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
) {
    if (out_read) *out_read = 0U;
    if (!tcp || !buf) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_tcp_is_connected(tcp)) return WET_HAL_ERR_IO;
    if (max_len == 0U) return WET_HAL_OK;

    int fd = (int)tcp->sock;
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;

    for (;;) {
        ssize_t n = recv(fd, buf, max_len, 0);
        if (n > 0) {
            if (out_read) *out_read = (size_t)n;
            return WET_HAL_OK;
        }
        if (n == 0) {
            return WET_HAL_ERR_IO;
        }
        if (errno == EINTR) {
            continue;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            uint64_t now_us = wet_hal_get_time_us();
            if (timeout_ms == 0U || now_us >= deadline_us) {
                return WET_HAL_ERR_TIMEOUT;
            }
            int rem_ms = (int)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms <= 0) rem_ms = 1;
            struct pollfd pfd;
            pfd.fd = fd;
            pfd.events = POLLIN;
            pfd.revents = 0;
            int prc = poll(&pfd, 1, rem_ms);
            if (prc < 0 && errno == EINTR) continue;
            if (prc == 0) return WET_HAL_ERR_TIMEOUT;
            if (prc < 0) return WET_HAL_ERR_IO;
            if ((pfd.revents & POLLIN) == 0 && (pfd.revents & (POLLERR | POLLHUP | POLLNVAL)) != 0) {
                return WET_HAL_ERR_IO;
            }
            continue;
        }
        return WET_HAL_ERR_IO;
    }
}

#endif /* _WIN32 */

/* =========================================================================
 * Platform-Independent Bounded Frame Read / Write Helpers
 * ========================================================================= */

wet_hal_status_t wet_hal_serial_write_frame(
    wet_hal_serial_t* ser,
    const char* frame,
    size_t len
) {
    if (!ser || !frame) return WET_HAL_ERR_NULL_PTR;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;

    size_t actual_len = (len > 0U) ? len : strlen(frame);
    if (actual_len > WET_HAL_TRANSPORT_MAX_FRAME) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    size_t written = 0U;
    if (actual_len > 0U) {
        wet_hal_status_t st = wet_hal_serial_write(ser, frame, actual_len, &written);
        if (st != WET_HAL_OK) return st;
    }
    if (actual_len == 0U || frame[actual_len - 1U] != '\r') {
        const char cr = '\r';
        wet_hal_status_t st = wet_hal_serial_write(ser, &cr, 1U, &written);
        if (st != WET_HAL_OK) return st;
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_serial_read_frame(
    wet_hal_serial_t* ser,
    char* out_buf,
    size_t buf_cap,
    uint32_t timeout_ms,
    size_t* out_len
) {
    if (out_len) *out_len = 0U;
    if (!ser || !out_buf) return WET_HAL_ERR_NULL_PTR;
    if (buf_cap == 0U) return WET_HAL_ERR_BUFFER_FULL;
    if (!wet_hal_serial_is_open(ser)) return WET_HAL_ERR_IO;

    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;
    size_t pos = 0U;

    for (;;) {
        uint64_t now_us = wet_hal_get_time_us();
        uint32_t rem_ms = 0U;
        if (timeout_ms > 0U) {
            if (now_us >= deadline_us) {
                out_buf[pos] = '\0';
                if (out_len) *out_len = pos;
                return WET_HAL_ERR_TIMEOUT;
            }
            rem_ms = (uint32_t)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms == 0U) rem_ms = 1U;
        }

        uint8_t ch = 0U;
        size_t got = 0U;
        wet_hal_status_t st = wet_hal_serial_read(ser, &ch, 1U, rem_ms, &got);
        if (st != WET_HAL_OK) {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return st;
        }
        if (got == 0U) continue;

        if ((char)ch == '\r') {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return WET_HAL_OK;
        }
        if (pos + 1U >= buf_cap) {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return WET_HAL_ERR_BUFFER_FULL;
        }
        out_buf[pos++] = (char)ch;
    }
}

wet_hal_status_t wet_hal_tcp_recv_frame(
    wet_hal_tcp_t* tcp,
    char* out_buf,
    size_t buf_cap,
    char delim,
    uint32_t timeout_ms,
    size_t* out_len
) {
    if (out_len) *out_len = 0U;
    if (!tcp || !out_buf) return WET_HAL_ERR_NULL_PTR;
    if (buf_cap == 0U) return WET_HAL_ERR_BUFFER_FULL;
    if (!wet_hal_tcp_is_connected(tcp)) return WET_HAL_ERR_IO;

    char eff_delim = (delim != '\0') ? delim : '\n';
    uint64_t deadline_us = wet_hal_get_time_us() + (uint64_t)timeout_ms * 1000ULL;
    size_t pos = 0U;

    for (;;) {
        uint64_t now_us = wet_hal_get_time_us();
        uint32_t rem_ms = 0U;
        if (timeout_ms > 0U) {
            if (now_us >= deadline_us) {
                out_buf[pos] = '\0';
                if (out_len) *out_len = pos;
                return WET_HAL_ERR_TIMEOUT;
            }
            rem_ms = (uint32_t)((deadline_us - now_us + 999ULL) / 1000ULL);
            if (rem_ms == 0U) rem_ms = 1U;
        }

        uint8_t ch = 0U;
        size_t got = 0U;
        wet_hal_status_t st = wet_hal_tcp_recv(tcp, &ch, 1U, rem_ms, &got);
        if (st != WET_HAL_OK) {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return st;
        }
        if (got == 0U) continue;

        if ((char)ch == eff_delim) {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return WET_HAL_OK;
        }
        if (pos + 1U >= buf_cap) {
            out_buf[pos] = '\0';
            if (out_len) *out_len = pos;
            return WET_HAL_ERR_BUFFER_FULL;
        }
        out_buf[pos++] = (char)ch;
    }
}
