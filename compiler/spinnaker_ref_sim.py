"""
WetLang Neuromorphic Backend - SpiNNaker PyNN Reference Simulator.
Pure-Python, zero-dependency implementation of the PyNN 0.9/0.10 API surface:
  - sim.setup / sim.run / sim.end / sim.reset
  - sim.Population / sim.Projection
  - Cell types: IF_cond_exp, IF_curr_exp, SpikeSourceArray, DCSource
  - Connectors: AllToAllConnector, OneToOneConnector, FromListConnector, FixedProbabilityConnector
  - Plasticity: STDPMechanism, SpikePairRule, AdditiveWeightDependence, StaticSynapse
  - Data containers: Neo-compatible Block / Segment / SpikeTrain / AnalogSignal

Provides deterministic biophysical simulation on Windows and non-SpiNNaker hosts.
"""

from typing import Any, Dict, List, Optional, Set, Tuple, Union
import math


# =========================================================================
# Neo-Compatible Data Containers for Recordings
# =========================================================================

class SpikeTrain(list):
    """Represents a train of spike timestamps for a single neuron."""
    def __init__(self, times: List[float], t_start: float = 0.0, t_stop: float = 1000.0, name: str = "spikes"):
        super().__init__(times)
        self.t_start = t_start
        self.t_stop = t_stop
        self.name = name
        self.units = "ms"
        self.annotations: Dict[str, Any] = {}

    @property
    def times(self) -> "SpikeTrain":
        return self


class AnalogSignal:
    """Represents continuous analog traces (e.g. membrane voltage V_m)."""
    def __init__(self, times: List[float], values: List[float], name: str = "v", units: str = "mV"):
        self.times = times
        self.magnitude = values
        self.name = name
        self.units = units

    def __len__(self) -> int:
        return len(self.magnitude)

    def __getitem__(self, idx: int) -> float:
        return self.magnitude[idx]


class Segment:
    """A segment of recorded neural data containing spiketrains and analog signals."""
    def __init__(self):
        self.spiketrains: List[SpikeTrain] = []
        self.analogsignals: List[AnalogSignal] = []

    def filter(self, name: Optional[str] = None) -> List[AnalogSignal]:
        if name is None:
            return self.analogsignals
        return [sig for sig in self.analogsignals if sig.name == name]


class Block:
    """Top-level container for PyNN recording data blocks."""
    def __init__(self):
        self.segments: List[Segment] = [Segment()]


# =========================================================================
# Neuron Models
# =========================================================================

class IF_cond_exp:
    """Conductance-based Leaky Integrate-and-Fire neuron with exponential synapses."""
    def __init__(
        self,
        v_rest: float = -70.0,
        v_thresh: float = -50.0,
        v_reset: float = -75.0,
        cm: float = 0.2,       # nF (equivalent to 200 pF)
        tau_m: float = 20.0,   # ms
        tau_syn_E: float = 5.0, # ms
        tau_syn_I: float = 5.0, # ms
        e_rev_E: float = 0.0,  # mV
        e_rev_I: float = -80.0, # mV
        i_offset: float = 0.0, # nA
        tau_refrac: float = 2.0, # ms
        tau_ahp: float = 80.0, # ms
        e_k: float = -90.0,    # mV
        **kwargs
    ):
        self.v_rest = float(v_rest)
        self.v_thresh = float(v_thresh)
        self.v_reset = float(v_reset)
        self.cm = float(cm)
        self.tau_m = float(tau_m)
        self.tau_syn_E = float(tau_syn_E)
        self.tau_syn_I = float(tau_syn_I)
        self.e_rev_E = float(e_rev_E)
        self.e_rev_I = float(e_rev_I)
        self.i_offset = float(i_offset)
        self.tau_refrac = float(tau_refrac)
        self.tau_ahp = float(tau_ahp)
        self.e_k = float(e_k)
        self.extra_params = kwargs


class IF_curr_exp:
    """Current-based Leaky Integrate-and-Fire neuron with exponential synapses."""
    def __init__(
        self,
        v_rest: float = -70.0,
        v_thresh: float = -50.0,
        v_reset: float = -75.0,
        cm: float = 0.2,
        tau_m: float = 20.0,
        tau_syn_E: float = 5.0,
        tau_syn_I: float = 5.0,
        i_offset: float = 0.0,
        tau_refrac: float = 2.0,
        tau_ahp: float = 80.0,
        e_k: float = -90.0,
        **kwargs
    ):
        self.v_rest = float(v_rest)
        self.v_thresh = float(v_thresh)
        self.v_reset = float(v_reset)
        self.cm = float(cm)
        self.tau_m = float(tau_m)
        self.tau_syn_E = float(tau_syn_E)
        self.tau_syn_I = float(tau_syn_I)
        self.i_offset = float(i_offset)
        self.tau_refrac = float(tau_refrac)
        self.tau_ahp = float(tau_ahp)
        self.e_k = float(e_k)
        self.extra_params = kwargs


class SpikeSourceArray:
    """Spike source emitting predefined timestamps."""
    def __init__(self, spike_times: Optional[Union[List[float], List[List[float]]]] = None):
        if spike_times is None:
            self.spike_times: List[List[float]] = [[]]
        elif isinstance(spike_times, list) and spike_times and isinstance(spike_times[0], list):
            self.spike_times = [sorted(float(t) for t in times) for times in spike_times]
        elif isinstance(spike_times, list):
            self.spike_times = [sorted(float(t) for t in spike_times)]
        else:
            self.spike_times = [[]]


class DCSource:
    """Constant injected direct current source."""
    def __init__(self, amplitude: float = 0.0, start: float = 0.0, stop: float = 1000.0):
        self.amplitude = float(amplitude)
        self.start = float(start)
        self.stop = float(stop)


# =========================================================================
# Connectors
# =========================================================================

class AllToAllConnector:
    def __init__(self, allow_self_connections: bool = True, safe: bool = True):
        self.allow_self_connections = allow_self_connections
        self.safe = safe

    def connect(self, pre_size: int, post_size: int) -> List[Tuple[int, int]]:
        pairs = []
        for i in range(pre_size):
            for j in range(post_size):
                if not self.allow_self_connections and i == j:
                    continue
                pairs.append((i, j))
        return pairs


class OneToOneConnector:
    def __init__(self, safe: bool = True):
        self.safe = safe

    def connect(self, pre_size: int, post_size: int) -> List[Tuple[int, int]]:
        return [(i, i) for i in range(min(pre_size, post_size))]


class FromListConnector:
    def __init__(self, conn_list: List[Tuple], safe: bool = True):
        self.conn_list = conn_list
        self.safe = safe

    def connect(self, pre_size: int, post_size: int) -> List[Tuple]:
        return list(self.conn_list)


class FixedProbabilityConnector:
    def __init__(self, p_connect: float = 0.1, allow_self_connections: bool = True, safe: bool = True):
        self.p_connect = float(p_connect)
        self.allow_self_connections = allow_self_connections
        self.safe = safe

    def connect(self, pre_size: int, post_size: int) -> List[Tuple[int, int]]:
        pairs = []
        for i in range(pre_size):
            for j in range(post_size):
                if not self.allow_self_connections and i == j:
                    continue
                pairs.append((i, j))
        return pairs


# =========================================================================
# Synapse Models & Plasticity
# =========================================================================

class StaticSynapse:
    def __init__(self, weight: float = 0.0, delay: Optional[float] = None):
        self.weight = float(weight)
        self.delay = float(delay) if delay is not None else 0.1


class SpikePairRule:
    def __init__(self, tau_plus: float = 20.0, tau_minus: float = 20.0, A_plus: float = 0.01, A_minus: float = 0.012):
        self.tau_plus = float(tau_plus)
        self.tau_minus = float(tau_minus)
        self.A_plus = float(A_plus)
        self.A_minus = float(A_minus)


class AdditiveWeightDependence:
    def __init__(self, w_min: float = 0.0, w_max: float = 1.0):
        self.w_min = float(w_min)
        self.w_max = float(w_max)


class STDPMechanism:
    """Spike-Timing-Dependent Plasticity synapse mechanism."""
    def __init__(
        self,
        timing_dependence: Optional[SpikePairRule] = None,
        weight_dependence: Optional[AdditiveWeightDependence] = None,
        voltage_dependence: Optional[Any] = None,
        dendritic_delay_fraction: Optional[float] = None,
        weight: Optional[float] = None,
        delay: Optional[float] = None,
    ):
        self.timing_dependence = timing_dependence or SpikePairRule()
        self.weight_dependence = weight_dependence or AdditiveWeightDependence()
        self.weight = float(weight) if weight is not None else 0.5
        self.delay = float(delay) if delay is not None else 0.1


# =========================================================================
# Simulation State
# =========================================================================

class _SimState:
    def __init__(self):
        self.timestep: float = 0.1     # ms
        self.min_delay: float = 0.1    # ms
        self.max_delay: float = 10.0   # ms
        self.current_time: float = 0.0 # ms
        self.populations: List["Population"] = []
        self.projections: List["Projection"] = []
        self.delay_queue: List[Tuple[float, "Projection", int, int, float]] = [] # (delivery_time, proj, pre_idx, post_idx, weight)

    def reset(self):
        self.current_time = 0.0
        self.delay_queue.clear()
        for pop in self.populations:
            pop._reset()


_SIM_STATE = _SimState()


# =========================================================================
# Population & Projection
# =========================================================================

class Population:
    """A homogeneous group of neural cells in PyNN."""
    def __init__(self, size: int, cellclass: Any, structure: Any = None, initial_values: Any = None, label: Optional[str] = None):
        self.size = int(size)
        self.cellclass = cellclass
        self.label = str(label or f"Population_{len(_SIM_STATE.populations)}")
        self.recorded_vars: Set[str] = set()

        # Recorded history
        self.spike_history: Dict[int, List[float]] = {i: [] for i in range(self.size)}
        self.v_history: Dict[int, List[Tuple[float, float]]] = {i: [] for i in range(self.size)}

        # Runtime state vectors
        self._reset()
        _SIM_STATE.populations.append(self)

    def _reset(self):
        self.spike_history = {i: [] for i in range(self.size)}
        self.v_history = {i: [] for i in range(self.size)}

        if isinstance(self.cellclass, (IF_cond_exp, IF_curr_exp)):
            self.v = [self.cellclass.v_rest] * self.size
            self.g_e = [0.0] * self.size
            self.g_i = [0.0] * self.size
            self.g_ahp = [0.0] * self.size
            self.refrac_time_left = [0.0] * self.size
        elif isinstance(self.cellclass, SpikeSourceArray):
            self.v = [0.0] * self.size
            self.g_e = [0.0] * self.size
            self.g_i = [0.0] * self.size
            self.g_ahp = [0.0] * self.size
            self.refrac_time_left = [0.0] * self.size
        else:
            self.v = [-70.0] * self.size
            self.g_e = [0.0] * self.size
            self.g_i = [0.0] * self.size
            self.g_ahp = [0.0] * self.size
            self.refrac_time_left = [0.0] * self.size

    def record(self, variables: Union[str, List[str]]) -> None:
        if isinstance(variables, str):
            self.recorded_vars.add(variables)
        else:
            for v in variables:
                self.recorded_vars.add(str(v))

    def get_data(self, variables: Optional[List[str]] = None, gather: bool = True, clear: bool = False) -> Block:
        blk = Block()
        seg = blk.segments[0]

        # Spiketrains
        for i in range(self.size):
            st = SpikeTrain(
                times=list(self.spike_history[i]),
                t_start=0.0,
                t_stop=_SIM_STATE.current_time,
                name=f"{self.label}_{i}"
            )
            seg.spiketrains.append(st)

        # Voltage AnalogSignals
        if "v" in self.recorded_vars or (variables and "v" in variables):
            for i in range(self.size):
                history = self.v_history[i]
                times = [pt[0] for pt in history]
                values = [pt[1] for pt in history]
                sig = AnalogSignal(times=times, values=values, name="v", units="mV")
                seg.analogsignals.append(sig)

        if clear:
            self._reset()
        return blk

    def get(self, parameter_names: Union[str, List[str]], gather: bool = True) -> Any:
        if isinstance(parameter_names, str):
            return getattr(self.cellclass, parameter_names, None)
        return {p: getattr(self.cellclass, p, None) for p in parameter_names}

    def set(self, **parameters) -> None:
        for k, v in parameters.items():
            setattr(self.cellclass, k, v)

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, idx: int) -> "Population":
        return self


class Projection:
    """A synaptic projection between presynaptic and postsynaptic populations."""
    def __init__(
        self,
        presynaptic_population: Population,
        postsynaptic_population: Population,
        connector: Any,
        synapse_type: Optional[Any] = None,
        source: Optional[str] = None,
        receptor_type: str = "excitatory",
        label: Optional[str] = None
    ):
        self.pre = presynaptic_population
        self.post = postsynaptic_population
        self.connector = connector
        self.synapse_type = synapse_type or StaticSynapse()
        self.receptor_type = receptor_type
        self.label = label or f"Projection_{len(_SIM_STATE.projections)}"

        # Materialize connection tuples: (pre_idx, post_idx, weight, delay)
        self.connections: List[Dict[str, Any]] = []
        raw_conns = connector.connect(len(self.pre), len(self.post))

        default_weight = getattr(self.synapse_type, "weight", 0.5)
        default_delay = getattr(self.synapse_type, "delay", 0.1)

        for item in raw_conns:
            if len(item) == 2:
                pre_i, post_j = item
                w = default_weight
                d = default_delay
            elif len(item) == 4:
                pre_i, post_j, w, d = item
            elif len(item) == 3:
                pre_i, post_j, w = item
                d = default_delay
            else:
                continue

            self.connections.append({
                "pre": int(pre_i),
                "post": int(post_j),
                "weight": float(w),
                "delay": float(d),
                "pre_trace": 0.0,
                "post_trace": 0.0
            })

        _SIM_STATE.projections.append(self)

    def get(self, names: Union[str, List[str]], format: str = "list", gather: bool = True) -> Any:
        if isinstance(names, str):
            names = [names]
        result = []
        for conn in self.connections:
            row = [conn[name] for name in names if name in conn]
            result.append(row if len(row) > 1 else row[0] if row else None)
        return result

    def set(self, **kwargs) -> None:
        for k, v in kwargs.items():
            for conn in self.connections:
                if k in conn:
                    conn[k] = float(v)


# =========================================================================
# Top-Level PyNN Simulation Interface Functions
# =========================================================================

def setup(timestep: float = 0.1, min_delay: float = 0.1, max_delay: float = 10.0, **kwargs) -> None:
    _SIM_STATE.timestep = float(timestep)
    _SIM_STATE.min_delay = float(min_delay)
    _SIM_STATE.max_delay = float(max_delay)
    _SIM_STATE.current_time = 0.0
    _SIM_STATE.populations.clear()
    _SIM_STATE.projections.clear()
    _SIM_STATE.delay_queue.clear()


def get_time_step() -> float:
    return _SIM_STATE.timestep


def get_current_time() -> float:
    return _SIM_STATE.current_time


def get_min_delay() -> float:
    return _SIM_STATE.min_delay


def get_max_delay() -> float:
    return _SIM_STATE.max_delay


def num_processes() -> int:
    return 1


def rank() -> int:
    return 0


def reset() -> None:
    _SIM_STATE.reset()


def end() -> None:
    pass


def run(sim_time: float) -> float:
    """
    Advances simulation time by sim_time (ms) using discrete integration.
    Handles synaptic conduction delays, LIF membrane updates, refractory tracking,
    and STDP weight modifications.
    """
    dt = _SIM_STATE.timestep
    steps = int(math.ceil(sim_time / dt))
    end_time = _SIM_STATE.current_time + sim_time

    for _ in range(steps):
        t = _SIM_STATE.current_time

        # 1. Check for incoming spikes from delay queue arriving at time <= t + dt/2
        incoming_syn: Dict[Tuple[int, int], float] = {} # (pop_id, neuron_idx) -> total current / conductance jump
        remaining_queue = []
        for arrival_t, proj, pre_idx, post_idx, w in _SIM_STATE.delay_queue:
            if arrival_t <= t + 1e-6:
                key = (id(proj.post), post_idx)
                incoming_syn[key] = incoming_syn.get(key, 0.0) + w
            else:
                remaining_queue.append((arrival_t, proj, pre_idx, post_idx, w))
        _SIM_STATE.delay_queue = remaining_queue

        # 2. Step populations & detect spikes
        current_step_spikes: Dict[int, Set[int]] = {} # pop_id -> set of spiking neuron indices

        for pop in _SIM_STATE.populations:
            current_step_spikes[id(pop)] = set()

            if isinstance(pop.cellclass, SpikeSourceArray):
                for i in range(pop.size):
                    stimes = pop.cellclass.spike_times[i] if i < len(pop.cellclass.spike_times) else []
                    for st in stimes:
                        if (t - 1e-9) <= st < (t + dt - 1e-9):
                            pop.spike_history[i].append(t)
                            current_step_spikes[id(pop)].add(i)
                continue

            # Standard LIF model (IF_cond_exp / IF_curr_exp) with AHP adaptation
            cc = pop.cellclass
            decay_syn_e = math.exp(-dt / max(getattr(cc, "tau_syn_E", 5.0), 1e-6))
            decay_syn_i = math.exp(-dt / max(getattr(cc, "tau_syn_I", 5.0), 1e-6))
            decay_ahp = math.exp(-dt / max(getattr(cc, "tau_ahp", 80.0), 1e-6))
            is_cond = isinstance(cc, IF_cond_exp)
            v_rest = getattr(cc, "v_rest", -70.0)
            e_k = getattr(cc, "e_k", -90.0)
            gl = getattr(cc, "cm", 0.2) / max(getattr(cc, "tau_m", 20.0), 1e-6)  # uS (0.2 nF / 20 ms = 0.01 uS = 10 nS)

            for i in range(pop.size):
                # Decay synaptic and AHP conductances
                pop.g_e[i] *= decay_syn_e
                pop.g_i[i] *= decay_syn_i
                pop.g_ahp[i] *= decay_ahp

                # Add incoming synaptic events
                input_w = incoming_syn.get((id(pop), i), 0.0)
                if input_w > 0.0:
                    pop.g_e[i] += input_w
                elif input_w < 0.0:
                    pop.g_i[i] += abs(input_w)

                # Refractory period check
                if pop.refrac_time_left[i] > 0.0:
                    pop.refrac_time_left[i] = max(0.0, pop.refrac_time_left[i] - dt)
                    pop.v[i] = cc.v_reset
                else:
                    if is_cond:
                        # Exact Exponential Euler COBA-LIF with AHP (conductances in uS, potentials in mV)
                        g_tot = max(gl + pop.g_e[i] + pop.g_i[i] + pop.g_ahp[i], 1e-9)
                        num = (
                            gl * v_rest
                            + pop.g_e[i] * cc.e_rev_E
                            + pop.g_i[i] * cc.e_rev_I
                            + pop.g_ahp[i] * e_k
                            + getattr(cc, "i_offset", 0.0)
                        )
                        v_inf = num / g_tot
                        tau_eff = max(getattr(cc, "cm", 0.2) / g_tot, 1e-6)
                        decay_v = math.exp(-dt / tau_eff)
                        pop.v[i] = v_inf + (pop.v[i] - v_inf) * decay_v
                    else:
                        decay_v = math.exp(-dt / max(getattr(cc, "tau_m", 20.0), 1e-6))
                        i_syn = pop.g_e[i] - pop.g_i[i]
                        i_total = i_syn + getattr(cc, "i_offset", 0.0)
                        pop.v[i] = v_rest + (pop.v[i] - v_rest) * decay_v + (i_total / max(gl, 1e-6)) * (1.0 - decay_v)

                    # Threshold detection
                    if pop.v[i] >= cc.v_thresh:
                        pop.v[i] = cc.v_reset
                        pop.refrac_time_left[i] = getattr(cc, "tau_refrac", 2.0)
                        pop.g_ahp[i] += 0.002  # 2.0 nS in uS
                        pop.spike_history[i].append(t)
                        current_step_spikes[id(pop)].add(i)

                # Record continuous voltage trace
                if "v" in pop.recorded_vars:
                    pop.v_history[i].append((t, pop.v[i]))

        # 3. Propagate spikes across Projections & Apply STDP
        for proj in _SIM_STATE.projections:
            pre_spikes = current_step_spikes.get(id(proj.pre), set())
            post_spikes = current_step_spikes.get(id(proj.post), set())
            is_stdp = isinstance(proj.synapse_type, STDPMechanism)

            for conn in proj.connections:
                pre_i = conn["pre"]
                post_j = conn["post"]

                # Check if presynaptic neuron spiked
                if pre_i in pre_spikes:
                    # Enqueue spike delivery with delay
                    arrival = t + conn["delay"]
                    _SIM_STATE.delay_queue.append((arrival, proj, pre_i, post_j, conn["weight"]))

                # STDP rule execution
                if is_stdp:
                    mech: STDPMechanism = proj.synapse_type
                    t_dep = mech.timing_dependence
                    w_dep = mech.weight_dependence
                    decay_p = math.exp(-dt / max(t_dep.tau_plus, 1e-6))
                    decay_m = math.exp(-dt / max(t_dep.tau_minus, 1e-6))

                    conn["pre_trace"] *= decay_p
                    conn["post_trace"] *= decay_m

                    if pre_i in pre_spikes:
                        conn["pre_trace"] += 1.0
                        # Post-then-pre -> LTD depression
                        if conn["post_trace"] > 0.0:
                            dw = -t_dep.A_minus * conn["post_trace"]
                            conn["weight"] = max(w_dep.w_min, min(w_dep.w_max, conn["weight"] + dw))

                    if post_j in post_spikes:
                        conn["post_trace"] += 1.0
                        # Pre-then-post -> LTP potentiation
                        if conn["pre_trace"] > 0.0:
                            dw = t_dep.A_plus * conn["pre_trace"]
                            conn["weight"] = max(w_dep.w_min, min(w_dep.w_max, conn["weight"] + dw))

        _SIM_STATE.current_time += dt

    return _SIM_STATE.current_time
