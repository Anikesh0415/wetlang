"""
WetLang PyTorch & NumPy Zero-Copy Tensor Interoperability Bridge (Project Janus - Sprint Task 1)
Provides zero-copy tensor sharing between C99 wetvm.dll memory buffers and PyTorch / NumPy arrays.
"""

from typing import Union, List, Optional, Tuple
import ctypes
import numpy as np

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    torch = None

from bindings.aer import WetAERPacket


def to_torch_tensor(arr: np.ndarray):
    """Converts a NumPy array view to a PyTorch Tensor if torch is installed."""
    if not TORCH_AVAILABLE:
        raise ImportError("PyTorch is not installed in the current environment. Please install torch.")
    # If array is a read-only ctypes view, use torch.tensor to avoid writeable warning
    if not arr.flags.writeable:
        return torch.tensor(arr)
    return torch.from_numpy(arr)


def spikes_tensor_to_aer_packets(
    spikes: Union[np.ndarray, "torch.Tensor", List[int]],
    timestamp_tick: int = 0,
    peak_amplitude_uv: int = 100,
    flags: int = 0,
) -> List[WetAERPacket]:
    """
    Converts incoming PyTorch/NumPy spike tensors into 16-byte aligned AER packets.
    Handles:
      1. Binary 64-channel activation vectors (e.g., shape (64,), non-zero entries denote firing).
      2. Explicit lists/tensors of firing channel indices (e.g., [0, 5, 23]).
    """
    if TORCH_AVAILABLE and isinstance(spikes, torch.Tensor):
        spikes = spikes.detach().cpu().numpy()
    elif isinstance(spikes, (list, tuple)):
        spikes = np.array(spikes)

    packets: List[WetAERPacket] = []

    # If 64-element array, treat as channel activity mask
    if spikes.ndim == 1 and len(spikes) == 64:
        active_channels = np.where(spikes > 0)[0]
        for ch in active_channels:
            pkt = WetAERPacket()
            pkt.timestamp_tick = timestamp_tick
            pkt.channel_id = int(ch)
            pkt.peak_amplitude_uv = int(peak_amplitude_uv)
            pkt.flags = int(flags)
            pkt.reserved = 0
            packets.append(pkt)
    else:
        # Array of channel IDs
        for ch in spikes.flatten():
            pkt = WetAERPacket()
            pkt.timestamp_tick = timestamp_tick
            pkt.channel_id = int(ch)
            pkt.peak_amplitude_uv = int(peak_amplitude_uv)
            pkt.flags = int(flags)
            pkt.reserved = 0
            packets.append(pkt)

    return packets
