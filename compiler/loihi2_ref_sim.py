"""
WetLang Neuromorphic Backend - Intel Loihi-2 Lava Reference Simulator.
Pure-Python, zero-dependency implementation of the Intel Lava API surface:
  - AbstractProcess
  - PyLoihiProcessModel / LoihiProcessModel
  - InPort / OutPort / PyInPort / PyOutPort
  - Var
  - RunSteps / PyExecCfg / RunConfig
  - LoihiProtocol / CPU / implements / requires / tag

Executes deterministic discrete COBA/CUBA-LIF integration and STDP weight accumulation.
"""

from typing import Any, Dict, List, Optional, Set, Tuple, Union
import math


class Var:
    """Represents a state variable or parameter in a Lava Process."""
    def __init__(self, shape: Tuple[int, ...] = (1,), init: Any = 0.0, name: str = "var"):
        self.shape = shape
        self.name = name
        if isinstance(init, (int, float)):
            total_elements = 1
            for dim in shape:
                total_elements *= dim
            self.value: Union[float, List[float]] = [float(init)] * total_elements if total_elements > 1 else float(init)
        elif isinstance(init, list):
            self.value = list(init)
        else:
            self.value = init

    def get(self) -> Any:
        return self.value

    def set(self, val: Any) -> None:
        self.value = val

    def __repr__(self) -> str:
        return f"Var(name={self.name!r}, shape={self.shape}, val={self.value!r})"


class InPort:
    """Input port for spike/current reception in a Lava Process."""
    def __init__(self, shape: Tuple[int, ...] = (1,), name: str = "in_port"):
        self.shape = shape
        self.name = name
        self._buffer: List[List[float]] = []
        self._connected_from: Optional["OutPort"] = None

    def recv(self) -> List[float]:
        total_elements = 1
        for dim in self.shape:
            total_elements *= dim
        if not self._buffer:
            return [0.0] * total_elements

        accum = [0.0] * total_elements
        while self._buffer:
            pkt = self._buffer.pop(0)
            for i, v in enumerate(pkt):
                if i < len(accum):
                    accum[i] += v
        return accum

    def __repr__(self) -> str:
        return f"InPort(name={self.name!r}, shape={self.shape})"


class OutPort:
    """Output port for spike/current transmission in a Lava Process."""
    def __init__(self, shape: Tuple[int, ...] = (1,), name: str = "out_port"):
        self.shape = shape
        self.name = name
        self._connected_to: List[InPort] = []

    def connect(self, in_port: InPort) -> None:
        if in_port not in self._connected_to:
            self._connected_to.append(in_port)
            in_port._connected_from = self

    def send(self, data: List[float]) -> None:
        for target in self._connected_to:
            target._buffer.append(list(data))

    def __repr__(self) -> str:
        return f"OutPort(name={self.name!r}, shape={self.shape})"


class PyInPort(InPort):
    VEC_DENSE = "VEC_DENSE"


class PyOutPort(OutPort):
    VEC_DENSE = "VEC_DENSE"


def LavaPyType(cls: Any, dtype: Any, precision: int = 32) -> Tuple[Any, Any, int]:
    return (cls, dtype, precision)


class CPU:
    pass


class LoihiProtocol:
    pass


def implements(proc: Any = None, protocol: Any = None):
    def decorator(cls):
        cls._implements_proc = proc
        cls._protocol = protocol
        if proc is not None:
            setattr(proc, "_default_model_cls", cls)
        return cls
    return decorator


def requires(*args, **kwargs):
    def decorator(cls):
        return cls
    return decorator


def tag(*args, **kwargs):
    def decorator(cls):
        return cls
    return decorator


class RunSteps:
    """Condition specifying the number of simulation steps to execute."""
    def __init__(self, num_steps: int = 100):
        self.num_steps = int(num_steps)


class PyExecCfg:
    """Execution configuration for CPU/PyLoihi execution."""
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class RunConfig:
    pass


# Global process and projection registries for deterministic reference simulation
_ACTIVE_PROCESSES: List["AbstractProcess"] = []
_ACTIVE_PROJECTIONS: List["SynapticProjection"] = []


def reset_processes() -> None:
    """Clears active Lava reference processes and synaptic projections."""
    _ACTIVE_PROCESSES.clear()
    _ACTIVE_PROJECTIONS.clear()


class SynapticProjection:
    """Delayed, channel-scoped, plastic synaptic projection between Lava Processes."""
    def __init__(
        self,
        pre: "AbstractProcess",
        post: "AbstractProcess",
        pre_idx: Optional[int] = None,
        post_idx: Optional[int] = None,
        weight: float = 0.5,
        delay_steps: int = 1,
        stdp_enabled: bool = False,
    ):
        self.pre = pre
        self.post = post
        self.pre_idx = int(pre_idx) if pre_idx is not None else None
        self.post_idx = int(post_idx) if post_idx is not None else None
        self.weight = float(weight)
        self.delay_steps = max(1, int(delay_steps))
        self.stdp_enabled = bool(stdp_enabled)
        self.delay_queue: List[Tuple[int, int, int, float]] = []  # (deliver_step, pre_i, post_j, weight)
        self.pre_trace: float = 0.0
        self.post_trace: float = 0.0
        _ACTIVE_PROJECTIONS.append(self)


class AbstractProcess:
    """Base class for Intel Lava Processes in the reference simulator."""
    _default_model_cls: Optional[Any] = None

    def __init__(self, **kwargs):
        self.proc_params: Dict[str, Any] = dict(kwargs)
        self.name: str = kwargs.get("name", self.__class__.__name__)
        self.spikes: List[List[float]] = []
        self.voltages: List[List[float]] = []
        self.current_step: int = 0
        self.model: Optional["PyLoihiProcessModel"] = None
        if self not in _ACTIVE_PROCESSES:
            _ACTIVE_PROCESSES.append(self)

    def add_projection(
        self,
        pre_proc: "AbstractProcess",
        pre_idx: Optional[int] = None,
        post_idx: Optional[int] = None,
        weight: float = 0.5,
        delay_steps: int = 1,
        stdp_enabled: bool = False,
    ) -> SynapticProjection:
        """Registers an incoming delayed synaptic projection onto this Process."""
        return SynapticProjection(
            pre=pre_proc,
            post=self,
            pre_idx=pre_idx,
            post_idx=post_idx,
            weight=weight,
            delay_steps=delay_steps,
            stdp_enabled=stdp_enabled,
        )

    def _ensure_model(self) -> "PyLoihiProcessModel":
        if self.model is None:
            model_cls = getattr(self.__class__, "_default_model_cls", None)
            if model_cls is None:
                model_cls = PyLoihiProcessModel
            self.model = model_cls(proc=self)
        return self.model

    def run(self, condition: Optional[RunSteps] = None, run_cfg: Optional[Any] = None) -> None:
        steps = condition.num_steps if isinstance(condition, RunSteps) else 100
        network: List["AbstractProcess"] = list(_ACTIVE_PROCESSES)

        for p in network:
            p._ensure_model()

        # Index which (pre, post) pairs have explicit SynapticProjections to avoid double-delivery
        explicit_pairs: Set[Tuple[int, int]] = set((id(pr.pre), id(pr.post)) for pr in _ACTIVE_PROJECTIONS)

        for _ in range(steps):
            # 1. Deliver delayed projection conductances scheduled for this step
            for proj in _ACTIVE_PROJECTIONS:
                if proj.post not in network or proj.post.model is None:
                    continue
                remaining = []
                for deliver_step, pre_i, post_j, w in proj.delay_queue:
                    if deliver_step <= proj.post.current_step:
                        # Scale WetLang normalized weight (~0.5-1.2) to nS excitatory conductance (~7.5-18 nS)
                        proj.post.model.g_exc[post_j] += max(0.0, w) * 15.0
                    else:
                        remaining.append((deliver_step, pre_i, post_j, w))
                proj.delay_queue = remaining

            # 2. Step all processes deterministically in insertion order
            step_spikes: Dict[int, List[float]] = {}
            for p in network:
                if p.model:
                    step_spikes[id(p)] = p.model.run_spk(suppress_outport=any(
                        pair[0] == id(p) for pair in explicit_pairs
                    ))

            # 3. Enqueue outgoing spikes along SynapticProjections and update inter-process STDP
            dt = 0.1
            for proj in _ACTIVE_PROJECTIONS:
                pre_spk = step_spikes.get(id(proj.pre))
                post_spk = step_spikes.get(id(proj.post))
                if pre_spk is None or post_spk is None:
                    continue
                pre_idx = (proj.pre_idx % len(pre_spk)) if proj.pre_idx is not None else None
                post_idx = (proj.post_idx % len(post_spk)) if proj.post_idx is not None else None

                pre_fired = (pre_spk[pre_idx] > 0.0) if pre_idx is not None else any(s > 0.0 for s in pre_spk)
                post_fired = (post_spk[post_idx] > 0.0) if post_idx is not None else any(s > 0.0 for s in post_spk)

                if pre_fired:
                    if post_idx is not None:
                        proj.delay_queue.append((proj.post.current_step + proj.delay_steps, pre_idx or 0, post_idx, proj.weight))
                    else:
                        for j in range(len(post_spk)):
                            proj.delay_queue.append((proj.post.current_step + proj.delay_steps, pre_idx or 0, j, proj.weight))

                if proj.stdp_enabled or getattr(proj.post, "stdp_enabled", False):
                    decay_p = math.exp(-dt / 20.0)
                    decay_m = math.exp(-dt / 20.0)
                    proj.pre_trace = proj.pre_trace * decay_p + (1.0 if pre_fired else 0.0)
                    proj.post_trace = proj.post_trace * decay_m + (1.0 if post_fired else 0.0)
                    dw = 0.0
                    if post_fired and proj.pre_trace > 0.0:
                        dw += 0.01 * proj.pre_trace
                    if pre_fired and proj.post_trace > 0.0:
                        dw -= 0.012 * proj.post_trace
                    if dw != 0.0:
                        proj.weight = max(0.0, min(2.0, proj.weight + dw))

            for p in network:
                p.current_step += 1

    def stop(self) -> None:
        pass

    def pause(self) -> None:
        pass

    def wait(self) -> None:
        pass


class PyLoihiProcessModel:
    """
    Deterministic reference execution model implementing discrete COBA-LIF integration
    with AHP adaptation, multi-tick channel stimulation, and STDP weight accumulation
    for Loihi-2 Lava processes.
    """
    def __init__(self, proc: AbstractProcess):
        self.proc = proc
        proc.model = self

        params = getattr(proc, "proc_params", {})
        self.n_neurons: int = int(getattr(proc, "n_neurons", params.get("n_neurons", params.get("cells", 100))))
        self.cm: float = float(getattr(proc, "cm", params.get("cm", 200.0)))
        self.gl: float = float(getattr(proc, "gl", params.get("gl", 10.0)))
        self.tau_m: float = float(getattr(proc, "tau_m", params.get("tau_m", 20.0)))
        self.e_leak: float = float(getattr(proc, "e_leak", params.get("e_leak", -70.0)))
        self.v_thresh: float = float(getattr(proc, "v_thresh", params.get("v_thresh", -50.0)))
        self.v_reset: float = float(getattr(proc, "v_reset", params.get("v_reset", -75.0)))
        self.e_exc: float = float(getattr(proc, "e_exc", params.get("e_exc", 0.0)))
        self.e_k: float = float(getattr(proc, "e_k", params.get("e_k", -90.0)))
        self.tau_exc: float = float(getattr(proc, "tau_exc", params.get("tau_exc", 5.0)))
        self.tau_ahp: float = float(getattr(proc, "tau_ahp", params.get("tau_ahp", 80.0)))
        self.refract_ticks_default: int = int(getattr(proc, "refractory_steps", params.get("refractory_steps", 20)))

        self.v: List[float] = [self.e_leak] * self.n_neurons
        self.g_exc: List[float] = [0.0] * self.n_neurons
        self.g_ahp: List[float] = [0.0] * self.n_neurons
        self.refractory_steps: List[int] = [0] * self.n_neurons

        self.stdp_enabled: bool = bool(getattr(proc, "stdp_enabled", params.get("stdp_enabled", False)))
        self.a_plus: float = float(getattr(proc, "a_plus", params.get("a_plus", 0.01)))
        self.a_minus: float = float(getattr(proc, "a_minus", params.get("a_minus", 0.012)))
        self.tau_plus: float = float(getattr(proc, "tau_plus", params.get("tau_plus", 20.0)))
        self.tau_minus: float = float(getattr(proc, "tau_minus", params.get("tau_minus", 20.0)))

        init_w = float(getattr(proc, "weight", params.get("weight", 0.5)))
        self.weights: List[List[float]] = [[init_w for _ in range(self.n_neurons)] for _ in range(self.n_neurons)]

        self.pre_trace: List[float] = [0.0] * self.n_neurons
        self.post_trace: List[float] = [0.0] * self.n_neurons
        self.external_stim: List[float] = [0.0] * self.n_neurons
        self.stim_amp: List[float] = [0.0] * self.n_neurons
        self.stim_ticks_left: List[int] = [0] * self.n_neurons

    def inject_stimulus(
        self,
        current_vector: Union[List[float], float, int],
        channel: Optional[int] = None,
        duration_steps: int = 1,
    ) -> None:
        dur = max(1, int(duration_steps))
        if isinstance(current_vector, (int, float)):
            amp = float(current_vector)
            if channel is not None:
                idx = int(channel) % max(1, self.n_neurons)
                if dur <= 1:
                    self.external_stim[idx] += amp
                else:
                    self.stim_amp[idx] = amp
                    self.stim_ticks_left[idx] = dur
            else:
                for i in range(self.n_neurons):
                    if dur <= 1:
                        self.external_stim[i] += amp
                    else:
                        self.stim_amp[i] = amp
                        self.stim_ticks_left[i] = dur
            return

        for i, val in enumerate(current_vector):
            if i < len(self.external_stim):
                if dur <= 1:
                    self.external_stim[i] += float(val)
                elif float(val) != 0.0:
                    self.stim_amp[i] = float(val)
                    self.stim_ticks_left[i] = dur

    def run_spk(self, suppress_outport: bool = False) -> List[float]:
        dt = 0.1
        decay_exc = math.exp(-dt / max(self.tau_exc, 1e-6))
        decay_ahp = math.exp(-dt / max(self.tau_ahp, 1e-6))
        decay_plus = math.exp(-dt / max(self.tau_plus, 1e-6))
        decay_minus = math.exp(-dt / max(self.tau_minus, 1e-6))

        s_in = [0.0] * self.n_neurons
        if hasattr(self.proc, "s_in") and isinstance(self.proc.s_in, InPort):
            recv_data = self.proc.s_in.recv()
            for i, val in enumerate(recv_data):
                if i < self.n_neurons:
                    s_in[i] += val

        i_syn = [0.0] * self.n_neurons
        for i in range(self.n_neurons):
            if s_in[i] > 0.0:
                for j in range(self.n_neurons):
                    i_syn[j] += s_in[i] * self.weights[i][j] * 100.0

        spikes = [0.0] * self.n_neurons
        for j in range(self.n_neurons):
            self.g_exc[j] *= decay_exc
            self.g_ahp[j] *= decay_ahp

            stim = self.external_stim[j]
            self.external_stim[j] = 0.0
            if self.stim_ticks_left[j] > 0:
                stim += self.stim_amp[j]
                self.stim_ticks_left[j] -= 1

            if self.refractory_steps[j] > 0:
                self.refractory_steps[j] -= 1
                self.v[j] = self.v_reset
            else:
                g_tot = max(self.gl + self.g_exc[j] + self.g_ahp[j], 1e-6)
                v_inf = (
                    self.gl * self.e_leak
                    + self.g_exc[j] * self.e_exc
                    + self.g_ahp[j] * self.e_k
                    + i_syn[j]
                    + stim
                ) / g_tot
                tau_eff = max(self.cm / g_tot, 1e-6)
                decay_v = math.exp(-dt / tau_eff)
                self.v[j] = v_inf + (self.v[j] - v_inf) * decay_v
                if self.v[j] >= self.v_thresh:
                    spikes[j] = 1.0
                    self.v[j] = self.v_reset
                    self.refractory_steps[j] = self.refract_ticks_default
                    self.g_ahp[j] += 2.0

        stdp_active = bool(self.stdp_enabled or getattr(self.proc, "stdp_enabled", False))
        if stdp_active:
            for i in range(self.n_neurons):
                self.pre_trace[i] = self.pre_trace[i] * decay_plus + s_in[i]
            for j in range(self.n_neurons):
                self.post_trace[j] = self.post_trace[j] * decay_minus + spikes[j]

            for i in range(self.n_neurons):
                for j in range(self.n_neurons):
                    dw = 0.0
                    if spikes[j] > 0.0 and self.pre_trace[i] > 0.0:
                        dw += self.a_plus * self.pre_trace[i]
                    if s_in[i] > 0.0 and self.post_trace[j] > 0.0:
                        dw -= self.a_minus * self.post_trace[j]
                    if dw != 0.0:
                        self.weights[i][j] = max(0.0, min(2.0, self.weights[i][j] + dw))

        if not suppress_outport and hasattr(self.proc, "s_out") and isinstance(self.proc.s_out, OutPort):
            self.proc.s_out.send(spikes)

        self.proc.spikes.append(list(spikes))
        self.proc.voltages.append(list(self.v))
        return spikes


class LoihiProcessModel(PyLoihiProcessModel):
    pass
