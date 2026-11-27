"""
WetLang Test Suite: Universal Python Wrapper & PyTorch Interoperability (Project Janus - Sprint Task 1)
Tests:
  - 1-line Python compilation: wl.compile(...)
  - 1-line VirtualMachine execution: wl.VirtualMachine(...)
  - Zero-copy NumPy views (voltages_numpy, spikes_numpy)
  - Zero-copy PyTorch Tensor interop (voltages_tensor, spikes_tensor)
  - Callable PyTorch loop: output_spikes = vm(input_spikes_tensor)
  - File loading: wl.load("benchmarks/01_active_inference_closed_loop.wet")
  - Context manager lifecycle: with wl.VirtualMachine(...) as vm:
  - Mirror package: from bindings.python import wetlang
"""

import pytest
import numpy as np
import torch

import wetlang as wl
from bindings.python import wetlang as wl_mirror


def test_import_and_version():
    """Verify top-level wetlang exports and version."""
    assert wl.__version__ == "2.2.0"
    assert wl_mirror.__version__ == "2.2.0"
    assert callable(wl.compile)
    assert callable(wl.load)
    assert hasattr(wl, "VirtualMachine")


def test_compile_and_virtual_machine_lifecycle():
    """Verify 1-line compilation and VM execution."""
    src = "grid mea[8, 8]; sync_tick();"
    bc = wl.compile(src)
    assert isinstance(bc, bytes)
    assert bc[:4] == b"WETB"

    with wl.VirtualMachine(bc, target="sim") as vm:
        assert vm.current_tick == 0
        telem = vm.step_tick()
        assert vm.current_tick == 1
        assert len(telem.voltages) == 64
        assert len(telem.spikes) == 64


def test_direct_source_string_instantiation():
    """Verify passing source code directly to VirtualMachine."""
    src = "grid mea[8, 8]; int i = 0; while (i < 5) { sync_tick(); i = i + 1; }"
    with wl.VirtualMachine(src) as vm:
        telem = vm.step_ticks(5)
        assert vm.current_tick == 5


def test_numpy_and_pytorch_zero_copy_views():
    """Verify NumPy array views and PyTorch zero-copy tensors."""
    src = "grid mea[8, 8]; sync_tick();"
    with wl.VirtualMachine(src) as vm:
        vm.step_tick()

        # NumPy views
        v_np = vm.voltages_numpy()
        s_np = vm.spikes_numpy()
        assert isinstance(v_np, np.ndarray)
        assert isinstance(s_np, np.ndarray)
        assert v_np.shape == (64,)
        assert s_np.shape == (64,)

        # PyTorch tensors
        v_torch = vm.voltages_tensor()
        s_torch = vm.spikes_tensor()
        assert isinstance(v_torch, torch.Tensor)
        assert isinstance(s_torch, torch.Tensor)
        assert v_torch.shape == (64,)
        assert s_torch.shape == (64,)

        # Spikes zero-copy verification: memory pointers match
        assert s_torch.data_ptr() == s_np.ctypes.data


def test_callable_pytorch_loop():
    """Verify vm(input_spikes_tensor) callable interface."""
    src = "grid mea[8, 8]; channel c = mea[2]; stim_biphasic(c, 0.4V, 0.1ms, 0.1ms); sync_tick();"
    with wl.VirtualMachine(src) as vm:
        # Create input spike tensor for channel 2
        in_spikes = torch.zeros(64, dtype=torch.float32)
        in_spikes[2] = 1.0

        out_spikes = vm(in_spikes)
        assert isinstance(out_spikes, torch.Tensor)
        assert out_spikes.shape == (64,)
        assert vm.current_tick == 1


def test_load_benchmark_file():
    """Verify wl.load on a benchmark .wet file."""
    with wl.load("benchmarks/01_active_inference_closed_loop.wet") as vm:
        assert vm.current_tick == 0
        vm.step_ticks(10)
        assert vm.current_tick == 10
