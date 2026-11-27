#ifndef WET_HAL_TRANSPORT_H
#define WET_HAL_TRANSPORT_H

#include <stdint.h>
#include <stddef.h>
#include "wet_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

#define WET_HAL_TRANSPORT_MAX_PATH 256
#define WET_HAL_TRANSPORT_MAX_FRAME 512

typedef struct {
    uintptr_t os_handle;       /* Win32 HANDLE ((uintptr_t)-1 when closed), 0 on POSIX */
    int32_t   fd;              /* POSIX fd (-1 when closed), -1 on Win32 */
    uint32_t  baud_rate;       /* Requested baud rate (e.g. 9600..115200) */
    uint32_t  timeout_ms;      /* Default read/frame timeout in ms */
    uint8_t   is_open;         /* 1 if open */
    uint8_t   is_pipe;         /* 1 if Win32 FILE_TYPE_PIPE (Named Pipe) or non-tty */
    uint8_t   _reserved[2];
    char      port_name[WET_HAL_TRANSPORT_MAX_PATH];
} wet_hal_serial_t;

typedef struct {
    uintptr_t sock;            /* SOCKET on Win32 (~(uintptr_t)0 when closed), or (uintptr_t)fd on POSIX */
    uint32_t  timeout_ms;      /* Default I/O timeout in ms */
    uint16_t  port;            /* Remote TCP port */
    uint8_t   is_connected;    /* 1 if connected */
    uint8_t   wsa_acquired;    /* 1 if Win32 WSAStartup ref held by this handle */
    char      host[WET_HAL_TRANSPORT_MAX_PATH];
} wet_hal_tcp_t;

/* Port path normalization (on _WIN32 normalizes COM10+ -> \\.\COM10+, preserves \\.\pipe\... & \\.\COMn) */
WET_EXPORT wet_hal_status_t wet_hal_transport_normalize_port(
    const char* port_name,
    char* out_buf,
    size_t buf_cap
);

/* Serial / Win32 Named Pipe / POSIX TTY (openpty) Transport API */
WET_EXPORT void wet_hal_serial_init(wet_hal_serial_t* ser);
WET_EXPORT wet_hal_status_t wet_hal_serial_open(
    wet_hal_serial_t* ser,
    const char* port_name,
    uint32_t baud_rate,
    uint32_t timeout_ms
);
WET_EXPORT void wet_hal_serial_close(wet_hal_serial_t* ser);
WET_EXPORT int wet_hal_serial_is_open(const wet_hal_serial_t* ser);
WET_EXPORT wet_hal_status_t wet_hal_serial_write(
    wet_hal_serial_t* ser,
    const void* data,
    size_t len,
    size_t* out_written
);
WET_EXPORT wet_hal_status_t wet_hal_serial_read(
    wet_hal_serial_t* ser,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
);
/* Writes ASCII frame (uses strlen if len==0; appends '\r' if not already '\r'-terminated) */
WET_EXPORT wet_hal_status_t wet_hal_serial_write_frame(
    wet_hal_serial_t* ser,
    const char* frame,
    size_t len
);
/* Reads bounded ASCII frame until '\r' (strips '\r', NUL-terminates out_buf, *out_len = payload bytes).
 * Returns WET_HAL_ERR_BUFFER_FULL if buf_cap exhausted before '\r', WET_HAL_ERR_TIMEOUT on deadline,
 * WET_HAL_ERR_IO on EOF/broken pipe/device error. */
WET_EXPORT wet_hal_status_t wet_hal_serial_read_frame(
    wet_hal_serial_t* ser,
    char* out_buf,
    size_t buf_cap,
    uint32_t timeout_ms,
    size_t* out_len
);

/* Non-Blocking TCP Socket Transport API */
WET_EXPORT void wet_hal_tcp_init(wet_hal_tcp_t* tcp);
WET_EXPORT wet_hal_status_t wet_hal_tcp_connect(
    wet_hal_tcp_t* tcp,
    const char* host,
    uint16_t port,
    uint32_t timeout_ms
);
WET_EXPORT void wet_hal_tcp_close(wet_hal_tcp_t* tcp);
WET_EXPORT int wet_hal_tcp_is_connected(const wet_hal_tcp_t* tcp);
WET_EXPORT wet_hal_status_t wet_hal_tcp_send_all(
    wet_hal_tcp_t* tcp,
    const void* data,
    size_t len,
    uint32_t timeout_ms,
    size_t* out_sent
);
WET_EXPORT wet_hal_status_t wet_hal_tcp_recv(
    wet_hal_tcp_t* tcp,
    void* buf,
    size_t max_len,
    uint32_t timeout_ms,
    size_t* out_read
);
/* Reads until `delim` (defaults to '\n' if delim == '\0'), strips `delim`, NUL-terminates. */
WET_EXPORT wet_hal_status_t wet_hal_tcp_recv_frame(
    wet_hal_tcp_t* tcp,
    char* out_buf,
    size_t buf_cap,
    char delim,
    uint32_t timeout_ms,
    size_t* out_len
);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_TRANSPORT_H */
