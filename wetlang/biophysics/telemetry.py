"""
WetLang Telemetry Streaming Engine
Provides JSONL and CSV logging for cycle-accurate biological digital twin state,
including membrane potentials, spike rasters, population firing rates, and net charges.
"""

import json
from typing import Any, Dict, List, Optional


class TelemetryStream:
    """
    Structured telemetry serialization engine for JSONL and CSV streaming formats.
    """

    def format_tick_json(
        self,
        tick: int,
        time_ms: float,
        v_m: Optional[List[float]] = None,
        spikes: Optional[List[int]] = None,
        population_rate_hz: float = 0.0,
        charges_nc: Optional[List[float]] = None,
        **kwargs: Any,
    ) -> str:
        """Serializes a single simulation cycle record to a JSONL-compliant line."""
        record: Dict[str, Any] = {
            "tick": tick,
            "time_ms": round(time_ms, 5),
            "v_m": v_m if v_m is not None else [],
            "spikes": spikes if spikes is not None else [],
            "population_rate_hz": population_rate_hz,
            "charges_nc": charges_nc if charges_nc is not None else [],
        }
        record.update(kwargs)
        return json.dumps(record)

    def get_csv_header(self) -> str:
        """Returns standard CSV telemetry summary header."""
        return "tick,time_ms,spike_count,r_inst_hz\n"

    def make_record(
        self,
        tick: int,
        time_ms: Optional[float] = None,
        spike_count: int = 0,
        population_rate_hz: float = 0.0,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Creates a structured in-memory dictionary record for a given simulation tick."""
        t_ms = time_ms if time_ms is not None else tick * 0.1
        rec: Dict[str, Any] = {
            "tick": tick,
            "time_ms": t_ms,
            "spike_count": spike_count,
            "population_rate_hz": population_rate_hz,
        }
        rec.update(kwargs)
        return rec

    def format_spike_event(
        self,
        tick: int,
        time_ms: float,
        neuron_id: int,
        neuron_type: str,
    ) -> str:
        """Formats a single sparse spike event for CSV logging: 'tick,time_ms,neuron_id,neuron_type'."""
        return f"{tick},{time_ms:.1f},{neuron_id},{neuron_type}"

    def compute_firing_rate(
        self,
        spike_count: int,
        neuron_count: int = 64,
        dt_ms: float = 0.1,
    ) -> float:
        """
        Calculates instantaneous population firing rate in Hertz (spikes / sec / neuron).
        r = spike_count / (neuron_count * (dt_ms / 1000.0))
        """
        if neuron_count <= 0 or dt_ms <= 0.0:
            return 0.0
        dt_sec = dt_ms / 1000.0
        return float(spike_count) / (neuron_count * dt_sec)
