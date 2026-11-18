"""
Universal Multi-Organoid Sandbox (1 to N Organoids)
===================================================
Orchestrates arbitrary multi-organoid connectomes, spatial networks,
axonal conduction delays, and microfluidic life-support telemetry.
Scales dynamically from 1 organoid to thousands of interconnected nodes.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any, Union
import numpy as np
import time

from bindings.runtime import WetRuntime, WetVM, WetVMError
from bindings.ffi import WetStatus


@dataclass
class AxonalTract:
    """Represents a biological or microfluidic axonal tract between two organoids."""
    source_id: int
    source_channel: int
    target_id: int
    target_channel: int
    conduction_delay_ticks: int
    synaptic_weight: float
    plasticity_enabled: bool = True


@dataclass
class OrganoidNode:
    """Represents a distinct 3D brain organoid unit on an MEA / microfluidic well."""
    organoid_id: int
    name: str
    cells: int
    radius_um: float
    perfusion_ul_min: float
    runtime: WetRuntime = field(default_factory=WetRuntime)
    is_alive: bool = True
    anoxia_events: int = 0
    total_spikes: int = 0
    last_voltages: np.ndarray = field(default_factory=lambda: np.zeros(64, dtype=np.float32))
    last_spikes: np.ndarray = field(default_factory=lambda: np.zeros(64, dtype=np.uint8))


class UniversalOrganoidSandbox:
    """
    Universal Multi-Organoid Execution & Safety Sandbox.
    Supports scaling from 1 organoid to arbitrary parametric N-organoid clusters.
    """

    def __init__(self, dt_ms: float = 0.1):
        self.dt_ms = dt_ms
        self.current_tick: int = 0
        self.organoids: Dict[int, OrganoidNode] = {}
        self.name_to_id: Dict[str, int] = {}
        self.tracts: List[AxonalTract] = []
        # In-flight axonal spikes: (deliver_tick, target_id, target_ch, amplitude_v)
        self.inflight_spikes: List[Tuple[int, int, int, float]] = []

    def create_organoid(
        self,
        name: str,
        cells: int = 100_000,
        radius_um: float = 250.0,
        perfusion_ul_min: float = 2.5,
        bytecode: Optional[bytes] = None,
    ) -> int:
        """Instantiate a new organoid in the sandbox."""
        if name in self.name_to_id:
            raise ValueError(f"Organoid '{name}' already exists in sandbox")

        org_id = len(self.organoids)
        node = OrganoidNode(
            organoid_id=org_id,
            name=name,
            cells=cells,
            radius_um=radius_um,
            perfusion_ul_min=perfusion_ul_min,
        )

        # Krogh cylinder anoxia pre-check
        if radius_um > 200.0 and perfusion_ul_min < 0.8:
            node.anoxia_events += 1

        if bytecode is not None:
            node.runtime.load(bytecode)
        else:
            # Default empty bytecode: 1 sync_tick
            from compiler.emitter import BytecodeEmitter
            from compiler.isa import Opcode, Capability
            emitter = BytecodeEmitter()
            emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE | Capability.CAP_CLOSED_LOOP
            emitter.emit(Opcode.SYNC_TICK)
            node.runtime.load(emitter._build_wbc_binary())

        self.organoids[org_id] = node
        self.name_to_id[name] = org_id
        return org_id

    def create_cluster(
        self,
        base_name: str,
        count: int,
        cells_per_organoid: int = 50_000,
        radius_um: float = 200.0,
        perfusion_ul_min: float = 1.5,
    ) -> List[int]:
        """Instantiate a parametric cluster of N organoids."""
        ids = []
        for i in range(count):
            name = f"{base_name}_{i}"
            org_id = self.create_organoid(
                name=name,
                cells=cells_per_organoid,
                radius_um=radius_um,
                perfusion_ul_min=perfusion_ul_min,
            )
            ids.append(org_id)
        return ids

    def connect(
        self,
        source: str,
        target: str,
        source_channel: int = 0,
        target_channel: int = 0,
        delay_ms: float = 5.0,
        weight: float = 1.0,
    ) -> None:
        """Create a directed axonal connection between two organoids."""
        if source not in self.name_to_id:
            raise KeyError(f"Source organoid '{source}' not found")
        if target not in self.name_to_id:
            raise KeyError(f"Target organoid '{target}' not found")

        src_id = self.name_to_id[source]
        tgt_id = self.name_to_id[target]
        delay_ticks = max(1, int(delay_ms / self.dt_ms + 0.5))

        self.tracts.append(AxonalTract(
            source_id=src_id,
            source_channel=source_channel,
            target_id=tgt_id,
            target_channel=target_channel,
            conduction_delay_ticks=delay_ticks,
            synaptic_weight=weight,
        ))

    def inject_stimulus(
        self,
        organoid: Union[str, int],
        channel: int,
        voltage_v: float,
        phase1_ms: float = 0.2,
        phase2_ms: float = 0.2,
    ) -> None:
        """Inject biphasic stimulus onto designated organoid and MEA channel."""
        org_id = self.name_to_id[organoid] if isinstance(organoid, str) else organoid
        self.organoids[org_id].runtime.inject_stimulus(channel, voltage_v, phase1_ms, phase2_ms)

    def emit_spike(self, organoid: Union[str, int], channel: int) -> None:
        """Manually trigger an action potential on designated organoid channel."""
        org_id = self.name_to_id[organoid] if isinstance(organoid, str) else organoid
        org = self.organoids[org_id]
        if org.last_spikes is None:
            org.last_spikes = np.zeros(64, dtype=np.uint8)
        org.last_spikes[channel] = 1

    def step(self, ticks: int = 1) -> Dict[str, Any]:
        """Advance the entire multi-organoid cluster by specified ticks."""
        for _ in range(ticks):
            self.current_tick += 1

            # 1. Deliver pending in-flight axonal action potentials
            remaining_spikes = []
            for deliver_tick, tgt_id, tgt_ch, amp_v in self.inflight_spikes:
                if deliver_tick <= self.current_tick:
                    org = self.organoids.get(tgt_id)
                    if org and org.is_alive:
                        try:
                            # Deliver sub-threshold or supra-threshold EPSP pulse
                            org.runtime.inject_stimulus(tgt_ch, amp_v, 0.1, 0.1)
                        except WetVMError:
                            pass
                else:
                    remaining_spikes.append((deliver_tick, tgt_id, tgt_ch, amp_v))
            self.inflight_spikes = remaining_spikes

            # 2. Step all organoids
            for org_id, org in self.organoids.items():
                if not org.is_alive:
                    continue
                # Preserve any pre-injected spikes from caller before step
                pre_spikes = org.last_spikes.copy() if org.last_spikes is not None else None
                try:
                    telem = org.runtime.step(1)
                    org.last_voltages = telem.channel_voltages
                    if pre_spikes is not None and pre_spikes.any():
                        org.last_spikes = telem.spike_raster | pre_spikes
                    else:
                        org.last_spikes = telem.spike_raster
                    spk_count = int(org.last_spikes.sum())
                    org.total_spikes += spk_count
                except WetVMError as ex:
                    # Emergency trip or lockout on this specific organoid
                    org.is_alive = False

            # 3. Route new outbound spikes across axonal tracts
            for tract in self.tracts:
                src_org = self.organoids.get(tract.source_id)
                if src_org and src_org.is_alive:
                    if src_org.last_spikes[tract.source_channel] > 0:
                        # Schedule arrival at target after conduction delay
                        arrival = self.current_tick + tract.conduction_delay_ticks
                        # Voltage proportional to synaptic weight (0.3 V baseline EPSP)
                        amp = min(0.8, 0.3 * tract.synaptic_weight)
                        self.inflight_spikes.append((
                            arrival, tract.target_id, tract.target_channel, amp
                        ))

        # Return cluster-wide telemetry snapshot
        alive_count = sum(1 for o in self.organoids.values() if o.is_alive)
        total_spikes = sum(o.total_spikes for o in self.organoids.values())
        return {
            "tick": self.current_tick,
            "sim_time_ms": self.current_tick * self.dt_ms,
            "total_organoids": len(self.organoids),
            "alive_organoids": alive_count,
            "total_cluster_spikes": total_spikes,
            "active_axonal_tracts": len(self.tracts),
            "inflight_spikes_count": len(self.inflight_spikes),
        }

    def close(self) -> None:
        """Safely shut down all organoid runtimes."""
        for org in self.organoids.values():
            try:
                org.runtime.close()
            except Exception:
                pass
        self.organoids.clear()
        self.name_to_id.clear()
        self.tracts.clear()
        self.inflight_spikes.clear()
