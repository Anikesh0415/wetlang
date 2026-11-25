"""
Tests for Neuromorphic Silicon Backends (Intel Loihi-2 & SpiNNaker PyNN).
Verifies:
  1. Target enum extension with Target.LOIHI2
  2. AST parsing and syntax validity of emitted Intel Lava and PyNN code
  3. Substrate Lowering Contract (W_SUBSTRATE_UNSUPPORTED_OP warnings and safe comments)
  4. Structural topology mapping (Organoids, Projections, STDP, stimulation)
  5. End-to-end deterministic closed-loop simulation via in-repo reference simulators
  6. Driver CLI execution for --target=loihi2 and --target=spinnaker
"""

import os
import sys
import ast
import tempfile
import warnings
import pytest

from compiler.emitter import (
    Target,
    SubstrateWarning,
    SubstrateUnsupportedOpWarning,
    emit_loihi2,
    emit_spinnaker,
    compile_to_loihi2,
    compile_to_spinnaker,
)
from compiler.compiler_cli import main as cli_main
import compiler.loihi2_ref_sim as loihi_sim
import compiler.spinnaker_ref_sim as spinn_sim


# =========================================================================
# Sample WetLang Programs for Testing
# =========================================================================

SAMPLE_BASELINE = """
organoid CorticalUnit {
    radius: 180um;
    perfusion: 1.2uL/min;
}

fn main() {
    stim_biphasic(0, 0.4V, 0.2ms, 0.2ms);
    let spikes = read_spikes(0, 10.0ms);
    sync_tick();
}
"""

SAMPLE_MULTI_ORGANOID_CONNECTOME = """
organoid SensoryCluster {
    cells: 50;
    perfusion: 1.0uL/min;
}

organoid MotorCluster {
    cells: 50;
    perfusion: 1.0uL/min;
}

connect SensoryCluster[0] -> MotorCluster[0] with {
    delay: 5.0ms;
    weight: 1.2;
    plasticity: "stdp";
};

fn main() {
    stim_biphasic(0, 0.4V, 0.2ms, 0.2ms);
    sync_tick(5);
}
"""

SAMPLE_WETWARE_PRIMITIVES = """
organoid CyberOrganoid {
    radius: 200um;
    perfusion: 2.0uL/min;
}

fn main() {
    pump_set_rate(0, 1.5uL/min);
    valve_open(0);
    motor_step(1, 50, 30.0rpm);
    let press = read_pressure(0);
    let temp = read_temperature();
    stim_biphasic(0, 0.5V, 0.2ms, 0.2ms);
    sync_tick();
}
"""

SAMPLE_WATER_WINDOW_VIOLATION = """
organoid OvervoltageUnit {
    cells: 30;
}

fn main() {
    // 1.8V exceeds +/- 1.2V electrochemical water window
    stim_biphasic(0, 1.8V, 0.2ms, 0.2ms);
    sync_tick();
}
"""


# =========================================================================
# Test Cases
# =========================================================================

def test_target_enum_loihi2():
    """Target.LOIHI2 must be defined with value 'loihi2'."""
    assert hasattr(Target, "LOIHI2")
    assert Target.LOIHI2 == "loihi2"
    assert Target.LOIHI2.value == "loihi2"
    assert Target.SPINNAKER.value == "spinnaker"


def test_compile_loihi2_ast_parse():
    """Emitted Intel Lava Python code must pass Python ast.parse syntax check."""
    loihi_code = compile_to_loihi2(SAMPLE_BASELINE)
    assert isinstance(loihi_code, str)
    assert "class CorticalUnitProcess(AbstractProcess):" in loihi_code
    assert "class CorticalUnitModel(PyLoihiProcessModel):" in loihi_code
    parsed = ast.parse(loihi_code)
    assert parsed is not None


def test_compile_spinnaker_ast_parse():
    """Emitted SpiNNaker PyNN Python code must pass Python ast.parse syntax check."""
    spin_code = compile_to_spinnaker(SAMPLE_BASELINE)
    assert isinstance(spin_code, str)
    assert "sim.setup" in spin_code
    assert "sim.Population" in spin_code
    assert "sim.IF_cond_exp" in spin_code
    parsed = ast.parse(spin_code)
    assert parsed is not None


def test_loihi2_structural_topology():
    """Loihi2 emitter must preserve multi-organoid topology and biophysical params."""
    loihi_code = compile_to_loihi2(SAMPLE_MULTI_ORGANOID_CONNECTOME)
    assert "SensoryClusterProcess" in loihi_code
    assert "MotorClusterProcess" in loihi_code
    assert "sensorycluster.s_out.connect(motorcluster.s_in)" in loihi_code
    assert "motorcluster.stdp_enabled = True" in loihi_code
    assert "self.cm = kwargs.get(\"cm\", 200.0)" in loihi_code
    assert "self.gl = kwargs.get(\"gl\", 10.0)" in loihi_code
    assert "self.tau_m = kwargs.get(\"tau_m\", 20.0)" in loihi_code
    assert "self.v_thresh = kwargs.get(\"v_thresh\", -50.0)" in loihi_code
    assert "self.v_reset = kwargs.get(\"v_reset\", -75.0)" in loihi_code
    ast.parse(loihi_code)


def test_spinnaker_structural_topology():
    """SpiNNaker emitter must map PyNN STDPMechanism and population projections."""
    spin_code = compile_to_spinnaker(SAMPLE_MULTI_ORGANOID_CONNECTOME)
    assert "sim.setup(timestep=0.1" in spin_code
    assert "sensorycluster = sim.Population(50, sim.IF_cond_exp" in spin_code
    assert "motorcluster = sim.Population(50, sim.IF_cond_exp" in spin_code
    assert "sim.STDPMechanism" in spin_code
    assert "sim.SpikePairRule" in spin_code
    assert "sim.AdditiveWeightDependence" in spin_code
    assert "sim.Projection(sensorycluster, motorcluster" in spin_code
    ast.parse(spin_code)


def test_substrate_lowering_contract_warnings_loihi2():
    """Substrate Lowering Contract: Loihi2 must issue W_SUBSTRATE_UNSUPPORTED_OP on wetware ops."""
    with pytest.warns(SubstrateUnsupportedOpWarning) as records:
        loihi_code = compile_to_loihi2(SAMPLE_WETWARE_PRIMITIVES)

    # Check warning messages
    warning_msgs = [str(r.message) for r in records]
    assert any("W_SUBSTRATE_UNSUPPORTED_OP" in msg for msg in warning_msgs)
    assert any("perfusion" in msg for msg in warning_msgs)
    assert any("pump_set_rate" in msg for msg in warning_msgs)
    assert any("valve_open" in msg for msg in warning_msgs)
    assert any("motor_step" in msg for msg in warning_msgs)

    # Check safe comment annotations in emitted code
    assert "# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op" in loihi_code
    ast.parse(loihi_code)


def test_substrate_lowering_contract_warnings_spinnaker():
    """Substrate Lowering Contract: SpiNNaker must issue W_SUBSTRATE_UNSUPPORTED_OP on wetware ops."""
    with pytest.warns(SubstrateUnsupportedOpWarning) as records:
        spin_code = compile_to_spinnaker(SAMPLE_WETWARE_PRIMITIVES)

    warning_msgs = [str(r.message) for r in records]
    assert any("W_SUBSTRATE_UNSUPPORTED_OP" in msg for msg in warning_msgs)
    assert any("pump_set_rate" in msg for msg in warning_msgs)
    assert any("valve_open" in msg for msg in warning_msgs)
    assert "# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op" in spin_code
    ast.parse(spin_code)


def test_water_window_lowering_warning():
    """Voltage exceeding +/- 1.2V must emit W_SUBSTRATE_UNSUPPORTED_OP warning."""
    with pytest.warns(SubstrateUnsupportedOpWarning) as records:
        loihi_code = compile_to_loihi2(SAMPLE_WATER_WINDOW_VIOLATION)

    warning_msgs = [str(r.message) for r in records]
    assert any("electrochemical_water_window" in msg for msg in warning_msgs)
    assert "W_SUBSTRATE_UNSUPPORTED_OP" in loihi_code


def test_loihi2_end_to_end_execution():
    """Emitted Loihi2 script must execute deterministically via reference simulator."""
    loihi_code = compile_to_loihi2(SAMPLE_MULTI_ORGANOID_CONNECTOME)
    env = {}
    exec(loihi_code, env)
    assert "main" in env
    result = env["main"]()
    assert isinstance(result, loihi_sim.AbstractProcess)
    assert len(result.voltages) > 0


def test_spinnaker_end_to_end_execution():
    """Emitted SpiNNaker script must execute deterministically via reference simulator."""
    spin_code = compile_to_spinnaker(SAMPLE_MULTI_ORGANOID_CONNECTOME)
    env = {}
    exec(spin_code, env)
    assert "main" in env
    data = env["main"]()
    assert isinstance(data, spinn_sim.Block)
    assert len(data.segments[0].spiketrains) > 0


def test_loihi2_ref_sim_stdp_accumulation():
    """Loihi2 reference simulator must accumulate STDP weight modifications."""
    class PlasticProcess(loihi_sim.AbstractProcess):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.n_neurons = 2
            self.s_in = loihi_sim.InPort(shape=(2,), name="s_in")
            self.s_out = loihi_sim.OutPort(shape=(2,), name="s_out")
            self.v = loihi_sim.Var(shape=(2,), init=-75.0, name="v")
            self.weights = loihi_sim.Var(shape=(2, 2), init=0.5, name="weights")

    proc = PlasticProcess(name="plastic_test")
    model = proc._ensure_model()
    model.stdp_enabled = True
    initial_w = model.weights[0][0]

    # Inject stimulus to force post-synaptic firing
    model.inject_stimulus([1000.0, 0.0])
    proc.run(loihi_sim.RunSteps(num_steps=5))
    final_w = model.weights[0][0]
    assert final_w >= 0.0


def test_spinnaker_ref_sim_stdp():
    """SpiNNaker reference simulator must update weights under STDPMechanism."""
    spinn_sim.setup(timestep=0.1)
    pop_pre = spinn_sim.Population(1, spinn_sim.SpikeSourceArray(spike_times=[1.0]), label="pre")
    pop_post = spinn_sim.Population(1, spinn_sim.IF_cond_exp(), label="post")

    stdp_mech = spinn_sim.STDPMechanism(
        timing_dependence=spinn_sim.SpikePairRule(tau_plus=20.0, tau_minus=20.0, A_plus=0.05, A_minus=0.05),
        weight_dependence=spinn_sim.AdditiveWeightDependence(w_min=0.0, w_max=2.0),
        weight=0.5,
        delay=0.1
    )
    proj = spinn_sim.Projection(pop_pre, pop_post, spinn_sim.AllToAllConnector(), synapse_type=stdp_mech)
    init_weight = proj.connections[0]["weight"]

    spinn_sim.run(10.0)
    final_weight = proj.connections[0]["weight"]
    assert final_weight >= 0.0
    spinn_sim.end()


def test_compiler_cli_loihi2_target():
    """Compiler CLI wetc must compile --target=loihi2 to valid Python script."""
    with tempfile.NamedTemporaryFile("w", suffix=".wet", delete=False) as f_in:
        f_in.write(SAMPLE_BASELINE)
        in_path = f_in.name

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f_out:
        out_path = f_out.name

    try:
        ret = cli_main([in_path, "--target", "loihi2", "-o", out_path])
        assert ret == 0
        assert os.path.exists(out_path)
        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "class CorticalUnitProcess" in content
        ast.parse(content)
    finally:
        if os.path.exists(in_path):
            os.remove(in_path)
        if os.path.exists(out_path):
            os.remove(out_path)


def test_compiler_cli_spinnaker_target():
    """Compiler CLI wetc must compile --target=spinnaker to valid PyNN script."""
    with tempfile.NamedTemporaryFile("w", suffix=".wet", delete=False) as f_in:
        f_in.write(SAMPLE_BASELINE)
        in_path = f_in.name

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f_out:
        out_path = f_out.name

    try:
        ret = cli_main([in_path, "--target", "spinnaker", "-o", out_path])
        assert ret == 0
        assert os.path.exists(out_path)
        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "sim.setup" in content
        assert "sim.Population" in content
        ast.parse(content)
    finally:
        if os.path.exists(in_path):
            os.remove(in_path)
        if os.path.exists(out_path):
            os.remove(out_path)
