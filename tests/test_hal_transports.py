"""Cross-platform loopback tests for OS serial/Named-Pipe/PTY and non-blocking TCP transports."""

import ctypes
import os
import socket
import sys
import threading
import time
import pytest

from bindings.ffi import (
    WetHalMode,
    WetHalSerial,
    WetHalStatus,
    WetHalTcp,
    WetVMFFI,
)


def _open_serial_loopback_endpoint(counter: int):
    """Creates a platform-native loopback endpoint without skipping on any OS."""
    if sys.platform == "win32":
        kernel32 = ctypes.windll.kernel32
        pipe_name = f"\\\\.\\pipe\\wetlang_test_{os.getpid()}_{counter}_{int(time.time() * 1000)}"
        PIPE_ACCESS_DUPLEX = 0x00000003
        PIPE_TYPE_BYTE = 0x00000000
        PIPE_READMODE_BYTE = 0x00000000
        PIPE_WAIT = 0x00000000
        INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

        kernel32.CreateNamedPipeA.restype = ctypes.c_void_p
        kernel32.CreateNamedPipeA.argtypes = [
            ctypes.c_char_p,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_uint32,
            ctypes.c_void_p,
        ]
        kernel32.ConnectNamedPipe.restype = ctypes.c_int
        kernel32.ConnectNamedPipe.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        kernel32.ReadFile.restype = ctypes.c_int
        kernel32.ReadFile.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.POINTER(ctypes.c_uint32),
            ctypes.c_void_p,
        ]
        kernel32.WriteFile.restype = ctypes.c_int
        kernel32.WriteFile.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.POINTER(ctypes.c_uint32),
            ctypes.c_void_p,
        ]
        kernel32.FlushFileBuffers.restype = ctypes.c_int
        kernel32.FlushFileBuffers.argtypes = [ctypes.c_void_p]
        kernel32.DisconnectNamedPipe.restype = ctypes.c_int
        kernel32.DisconnectNamedPipe.argtypes = [ctypes.c_void_p]
        kernel32.CloseHandle.restype = ctypes.c_int
        kernel32.CloseHandle.argtypes = [ctypes.c_void_p]

        h_srv = kernel32.CreateNamedPipeA(
            pipe_name.encode("ascii"),
            PIPE_ACCESS_DUPLEX,
            PIPE_TYPE_BYTE | PIPE_READMODE_BYTE | PIPE_WAIT,
            1,
            4096,
            4096,
            1000,
            None,
        )
        assert h_srv is not None and h_srv != INVALID_HANDLE_VALUE

        def accept_client():
            kernel32.ConnectNamedPipe(h_srv, None)

        def read_bytes(n: int) -> bytes:
            buf = (ctypes.c_uint8 * n)()
            got = ctypes.c_uint32(0)
            ok = kernel32.ReadFile(h_srv, buf, n, ctypes.byref(got), None)
            if not ok:
                return b""
            return bytes(buf[:got.value])

        def write_bytes(payload: bytes) -> None:
            c_buf = (ctypes.c_uint8 * len(payload)).from_buffer_copy(payload)
            wrote = ctypes.c_uint32(0)
            kernel32.WriteFile(h_srv, c_buf, len(payload), ctypes.byref(wrote), None)

        def close_server() -> None:
            kernel32.DisconnectNamedPipe(h_srv)
            kernel32.CloseHandle(h_srv)

        return pipe_name, accept_client, read_bytes, write_bytes, close_server
    else:
        import pty
        import termios

        master_fd, slave_fd = pty.openpty()
        attrs = termios.tcgetattr(slave_fd)
        attrs[3] &= ~(termios.ECHO | termios.ICANON)
        termios.tcsetattr(slave_fd, termios.TCSANOW, attrs)
        slave_path = os.ttyname(slave_fd)

        def accept_client():
            return None

        def read_bytes(n: int) -> bytes:
            return os.read(master_fd, n)

        def write_bytes(payload: bytes) -> None:
            os.write(master_fd, payload)

        def close_server() -> None:
            try:
                os.close(slave_fd)
            except OSError:
                pass
            try:
                os.close(master_fd)
            except OSError:
                pass

        return slave_path, accept_client, read_bytes, write_bytes, close_server


def test_port_path_normalization():
    ffi = WetVMFFI()
    if sys.platform == "win32":
        st, out = ffi.transport_normalize_port("COM10")
        assert st == WetHalStatus.WET_HAL_OK and out == "\\\\.\\COM10"
        st, out = ffi.transport_normalize_port("com12")
        assert st == WetHalStatus.WET_HAL_OK and out == "\\\\.\\COM12"
        st, out = ffi.transport_normalize_port("\\\\.\\COM10")
        assert st == WetHalStatus.WET_HAL_OK and out == "\\\\.\\COM10"
        st, out = ffi.transport_normalize_port("\\\\.\\pipe\\test_pipe")
        assert st == WetHalStatus.WET_HAL_OK and out == "\\\\.\\pipe\\test_pipe"
        st, out = ffi.transport_normalize_port("COM1")
        assert st == WetHalStatus.WET_HAL_OK and out == "COM1"
    else:
        st, out = ffi.transport_normalize_port("/dev/ttyUSB0")
        assert st == WetHalStatus.WET_HAL_OK and out == "/dev/ttyUSB0"


def test_serial_cr_frame_loopback_and_timeout():
    ffi = WetVMFFI()
    path, accept_client, read_bytes, write_bytes, close_server = _open_serial_loopback_endpoint(1)
    received = bytearray()

    def server_worker():
        accept_client()
        while True:
            chunk = read_bytes(64)
            if not chunk:
                break
            received.extend(chunk)
            if b"\r" in received:
                break
        # Fragmented reply across two writes
        write_bytes(b"01")
        time.sleep(0.02)
        write_bytes(b">\r")

    t = threading.Thread(target=server_worker, daemon=True)
    t.start()

    ser = WetHalSerial()
    ffi.serial_init(ser)
    try:
        st = ffi.serial_open(ser, path, 115200, 500)
        assert st == WetHalStatus.WET_HAL_OK
        assert ffi.serial_is_open(ser)

        st = ffi.serial_write_frame(ser, "01 @irate 1.500 u/m\r")
        assert st == WetHalStatus.WET_HAL_OK

        st, reply = ffi.serial_read_frame(ser, buf_cap=64, timeout_ms=1000)
        assert st == WetHalStatus.WET_HAL_OK
        assert reply == "01>"

        # Silent server -> bounded timeout
        t0 = time.monotonic()
        st_to, _ = ffi.serial_read_frame(ser, buf_cap=64, timeout_ms=60)
        elapsed = time.monotonic() - t0
        assert st_to == WetHalStatus.WET_HAL_ERR_TIMEOUT
        assert elapsed < 0.8

        # Overflow buffer check
        write_bytes(b"0123456789\r")
        st_full, _ = ffi.serial_read_frame(ser, buf_cap=4, timeout_ms=500)
        assert st_full == WetHalStatus.WET_HAL_ERR_BUFFER_FULL

        t.join(timeout=2.0)
        assert bytes(received) == b"01 @irate 1.500 u/m\r"
    finally:
        ffi.serial_close(ser)
        close_server()


def test_serial_disconnect_returns_io_error():
    ffi = WetVMFFI()
    path, accept_client, _read_bytes, _write_bytes, close_server = _open_serial_loopback_endpoint(2)

    def server_worker():
        accept_client()
        time.sleep(0.02)
        close_server()

    t = threading.Thread(target=server_worker, daemon=True)
    t.start()

    ser = WetHalSerial()
    ffi.serial_init(ser)
    try:
        assert ffi.serial_open(ser, path, 115200, 500) == WetHalStatus.WET_HAL_OK
        t.join(timeout=2.0)
        st, _ = ffi.serial_read_frame(ser, buf_cap=64, timeout_ms=300)
        assert st == WetHalStatus.WET_HAL_ERR_IO
    finally:
        ffi.serial_close(ser)


def test_tcp_nonblocking_loopback_partial_frames_and_deadlines():
    ffi = WetVMFFI()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(("127.0.0.1", 0))
    srv.listen(2)
    port = srv.getsockname()[1]

    srv2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv2.bind(("127.0.0.1", 0))
    srv2.listen(1)
    port2 = srv2.getsockname()[1]

    # Closed port for immediate ECONNREFUSED / exceptfds verification
    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe.bind(("127.0.0.1", 0))
    closed_port = probe.getsockname()[1]
    probe.close()

    received_cmds = []

    def server_worker(sock_listen, send_banner=True):
        conn, _ = sock_listen.accept()
        with conn:
            data = conn.recv(128)
            received_cmds.append(data)
            if send_banner:
                conn.sendall(b"OK ")
                time.sleep(0.02)
                conn.sendall(b"READY\n")
                # Stay silent briefly so timeout test triggers cleanly
                time.sleep(0.2)

    t1 = threading.Thread(target=server_worker, args=(srv, True), daemon=True)
    t2 = threading.Thread(target=server_worker, args=(srv2, True), daemon=True)
    t1.start()
    t2.start()

    tcp1 = WetHalTcp()
    tcp2 = WetHalTcp()
    tcp_refused = WetHalTcp()
    ffi.tcp_init(tcp1)
    ffi.tcp_init(tcp2)
    ffi.tcp_init(tcp_refused)

    try:
        assert ffi.tcp_connect(tcp1, "127.0.0.1", port, 1000) == WetHalStatus.WET_HAL_OK
        assert ffi.tcp_is_connected(tcp1)
        assert ffi.tcp_connect(tcp2, "127.0.0.1", port2, 1000) == WetHalStatus.WET_HAL_OK
        assert ffi.tcp_is_connected(tcp2)

        # Closing tcp1 must not tear down Winsock refcount while tcp2 is active
        st_s1, sent1 = ffi.tcp_send_all(tcp1, b"PING\n", 500)
        assert st_s1 == WetHalStatus.WET_HAL_OK and sent1 == 5
        st_r1, msg1 = ffi.tcp_recv_frame(tcp1, buf_cap=64, delim=b"\n", timeout_ms=500)
        assert st_r1 == WetHalStatus.WET_HAL_OK and msg1 == "OK READY"

        # Silent timeout check
        st_to, _ = ffi.tcp_recv_frame(tcp1, buf_cap=64, delim=b"\n", timeout_ms=50)
        assert st_to == WetHalStatus.WET_HAL_ERR_TIMEOUT

        ffi.tcp_close(tcp1)
        assert not ffi.tcp_is_connected(tcp1)

        # tcp2 still works cleanly
        st_s2, sent2 = ffi.tcp_send_all(tcp2, b"PING2\n", 500)
        assert st_s2 == WetHalStatus.WET_HAL_OK and sent2 == 6
        st_r2, msg2 = ffi.tcp_recv_frame(tcp2, buf_cap=64, delim=b"\n", timeout_ms=500)
        assert st_r2 == WetHalStatus.WET_HAL_OK and msg2 == "OK READY"

        # Closed port fails fast via select exceptfds / SO_ERROR
        t0 = time.monotonic()
        timeout_ref = 3500 if sys.platform == "win32" else 2000
        st_ref = ffi.tcp_connect(tcp_refused, "127.0.0.1", closed_port, timeout_ref)
        assert st_ref == WetHalStatus.WET_HAL_ERR_IO
        max_dur = 3.0 if sys.platform == "win32" else 1.5
        assert (time.monotonic() - t0) < max_dur

        t1.join(timeout=2.0)
        t2.join(timeout=2.0)
        assert b"PING\n" in received_cmds
        assert b"PING2\n" in received_cmds
    finally:
        ffi.tcp_close(tcp1)
        ffi.tcp_close(tcp2)
        ffi.tcp_close(tcp_refused)
        srv.close()
        srv2.close()


def test_microfluidics_physical_mode_end_to_end():
    ffi = WetVMFFI()

    # Backward compatibility: WET_HAL_MODE_PHYSICAL without open_serial must still succeed
    drv_mem = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_PHYSICAL)
    assert drv_mem
    try:
        assert ffi.pump_set_rate(drv_mem, 0, 2.0, 1) == WetHalStatus.WET_HAL_OK
    finally:
        ffi.microfluidics_destroy(drv_mem)

    # Full physical transport loopback
    path, accept_client, read_bytes, write_bytes, close_server = _open_serial_loopback_endpoint(3)
    frames_seen = []

    def mock_harvard_pump():
        accept_client()
        buf = bytearray()
        while len(frames_seen) < 3:
            chunk = read_bytes(128)
            if not chunk:
                break
            buf.extend(chunk)
            while b"\r" in buf:
                idx = buf.index(b"\r")
                frame = bytes(buf[:idx]).decode("ascii", errors="replace")
                del buf[: idx + 1]
                frames_seen.append(frame)
                if len(frames_seen) == 1:
                    write_bytes(b"00>\r")
                elif len(frames_seen) == 2:
                    write_bytes(b"00*\r")  # Stall prompt on 2nd command
                else:
                    write_bytes(b"00:\r")  # Idle prompt on stop

    t = threading.Thread(target=mock_harvard_pump, daemon=True)
    t.start()

    drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_PHYSICAL)
    assert drv
    try:
        assert ffi.microfluidics_open_serial(drv, path, 115200, 500) == WetHalStatus.WET_HAL_OK
        assert ffi.pump_set_rate(drv, 0, 2.5, 1) == WetHalStatus.WET_HAL_OK

        # Closing downstream valve trips dead-head BEFORE serial transmit
        assert ffi.valve_set_state(drv, 0, 0) == WetHalStatus.WET_HAL_OK
        assert ffi.pump_set_rate(drv, 0, 3.0, 1) == WetHalStatus.WET_HAL_ERR_DEAD_HEAD
        assert ffi.valve_set_state(drv, 0, 1) == WetHalStatus.WET_HAL_OK

        # Mock pump responds with '*' -> WET_HAL_ERR_IO
        assert ffi.pump_set_rate(drv, 0, 3.5, 1) == WetHalStatus.WET_HAL_ERR_IO

        # Stop command sends @stp\r and gets ':' -> WET_HAL_OK
        assert ffi.pump_stop(drv, 0) == WetHalStatus.WET_HAL_OK

        t.join(timeout=2.0)
        assert frames_seen == ["@irate 2.500 u/m", "@irate 3.500 u/m", "@stp"]
    finally:
        ffi.microfluidics_close_serial(drv)
        ffi.microfluidics_destroy(drv)
        close_server()
