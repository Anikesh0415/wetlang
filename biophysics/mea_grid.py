"""
WetLang Biophysical Digital Twin: 8x8 MEA Grid Topology
Provides spatial mapping, electrode substrate coordinates, 3D volume conduction forward matrix,
and resistive cross-talk kernel for an 8x8 microelectrode array (200 um pitch).
"""

import math
from typing import Tuple
import numpy as np


class MEAGrid:
    """
    8x8 Microelectrode Array (MEA) with 200 um pitch.
    Total of 64 electrodes arranged in an 8x8 Cartesian topology.
    """

    def __init__(self, rows: int = 8, cols: int = 8, pitch_um: float = 200.0):
        self.rows: int = rows
        self.cols: int = cols
        self.pitch_um: float = pitch_um
        self.total_electrodes: int = rows * cols

    def coords_to_channel(self, row: int, col: int) -> int:
        """Bijective mapping from 2D (row, col) coordinates to 1D channel index."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError(f"Coordinates ({row}, {col}) out of MEA bounds ({self.rows}x{self.cols})")
        return row * self.cols + col

    def channel_to_coords(self, ch: int) -> Tuple[int, int]:
        """Bijective mapping from 1D channel index to 2D (row, col) coordinates."""
        if not (0 <= ch < self.total_electrodes):
            raise ValueError(f"Channel index {ch} out of bounds (0..{self.total_electrodes - 1})")
        return (ch // self.cols, ch % self.cols)

    def get_electrode_pos(self, ch: int) -> Tuple[float, float]:
        """
        Returns physical Cartesian substrate coordinates (x_um, y_um) of electrode center.
        Electrodes are centered at (col + 0.5) * pitch_um, (row + 0.5) * pitch_um.
        For 200 um pitch: ch 0 -> (100.0, 100.0), ch 63 -> (1500.0, 1500.0).
        """
        r, c = self.channel_to_coords(ch)
        x_um = (c + 0.5) * self.pitch_um
        y_um = (r + 0.5) * self.pitch_um
        return (x_um, y_um)

    def calculate_field_potential(
        self,
        source_x: float,
        source_y: float,
        source_z: float,
        current_na: float,
        sigma: float = 0.3,
        r0_um: float = 15.0,
    ) -> np.ndarray:
        """
        Calculates 3D volume conduction forward pickup potentials across all electrodes
        given a point current source in conductive extracellular medium (conductivity sigma in S/m).
        """
        potentials = np.zeros(self.total_electrodes, dtype=np.float64)
        for ch in range(self.total_electrodes):
            ex, ey = self.get_electrode_pos(ch)
            dx = source_x - ex
            dy = source_y - ey
            dz = source_z
            dist_um = math.sqrt(dx * dx + dy * dy + dz * dz + r0_um * r0_um)
            # Extracellular potential: V = I / (4 * pi * sigma * r)
            # I in nA (1e-9 A), dist in um (1e-6 m), sigma in S/m -> V in Volts
            v_volts = (current_na * 1e-9) / (4.0 * math.pi * sigma * (dist_um * 1e-6))
            potentials[ch] = v_volts

        return potentials

    def get_crosstalk_matrix(self) -> np.ndarray:
        """
        Returns 64x64 resistive cross-talk matrix between electrodes.
        Self-coupling is 1.0; 4-way adjacent electrodes have ~0.04 resistive coupling.
        """
        mat = np.zeros((self.total_electrodes, self.total_electrodes), dtype=np.float64)
        for i in range(self.total_electrodes):
            r1, c1 = self.channel_to_coords(i)
            for j in range(self.total_electrodes):
                if i == j:
                    mat[i, j] = 1.0
                else:
                    r2, c2 = self.channel_to_coords(j)
                    manhattan_dist = abs(r1 - r2) + abs(c1 - c2)
                    if manhattan_dist == 1:
                        mat[i, j] = 0.04
                    else:
                        euclid_dist = math.sqrt((r1 - r2) ** 2 + (c1 - c2) ** 2)
                        mat[i, j] = 0.04 / (euclid_dist ** 2)

        return mat
