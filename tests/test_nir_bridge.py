"""
WetLang Test Suite: Neuromorphic Intermediate Representation (NIR v1.0) Bridge
Verifies bidirectional translation, Dale's principle enforcement, biophysical
parameter mappings, HDF5/JSON round-trips, and native C99 VM execution.
"""

import tempfile
from pathlib import Path
import pytest
import numpy as np

from compiler.nir_bridge import (
    NIRGraph,
    Input,
    Output,
    Linear,
    Affine,
    LIF,
    CubaLIF,
    Izhikevich,
    DalesPrincipleError,
    NIRValidationError,
    validate_dales_principle,
    enforce_dales_principle,
    decompose_to_dales_principle,
    save_nir_hdf5,
    load_nir_hdf5,
    save_nir_json,
    load_nir_json,
    nir_to_wet_source,
    nir_to_wet_ast,
    nir_to_wet_bytecode,
    wet_ast_to_nir,
    wet_bytecode_to_nir,
    wet_vm_to_nir,
    load_nir_into_vm,
    WET_TAU_MEM_MS,
    WET_TAU_SYN_AMPA_MS,
    WET_TAU_SYN_GABA_MS,
    WET_V_LEAK_MV,
    WET_V_RESET_MV,
    WET_V_THRESH_MV,
    IZHIKEVICH_RS,
    IZHIKEVICH_FS,
)
from compiler.ast_nodes import ProgramNode
from compiler.isa import HEADER_MAGIC
from bindings.runtime import WetRuntime, WetVM


# =========================================================================
# 1. Standard Node Primitives & Biophysical Parameter Mappings
# =========================================================================

def test_cubalif_biophysical_parameters():
    """Verify CubaLIF biophysical parameters match WetLang COBA-LIF model."""
    node = CubaLIF()
    assert float(node.tau_mem[0]) == pytest.approx(WET_TAU_MEM_MS)  # 20.0 ms
    assert float(node.tau_syn[0]) == pytest.approx(WET_TAU_SYN_AMPA_MS)  # 5.0 ms
    assert float(node.v_leak[0]) == pytest.approx(WET_V_LEAK_MV)  # -70.0 mV
    assert float(node.v_reset[0]) == pytest.approx(WET_V_RESET_MV)  # -75.0 mV
    assert float(node.v_threshold[0]) == pytest.approx(WET_V_THRESH_MV)  # -50.0 mV


def test_lif_parameters():
    """Verify LIF parameters map to instantaneous conductance impulse."""
    node = LIF()
    assert float(node.tau[0]) == pytest.approx(WET_TAU_MEM_MS)
    assert float(node.v_leak[0]) == pytest.approx(WET_V_LEAK_MV)
    assert float(node.v_reset[0]) == pytest.approx(WET_V_RESET_MV)
    assert float(node.v_threshold[0]) == pytest.approx(WET_V_THRESH_MV)


def test_izhikevich_cortical_phenotypes():
    """Verify Izhikevich mappings for cortical RS (excitatory) and FS (inhibitory)."""
    rs_node = Izhikevich(
        a=np.array([IZHIKEVICH_RS["a"]]),
        b=np.array([IZHIKEVICH_RS["b"]]),
        c=np.array([IZHIKEVICH_RS["c"]]),
        d=np.array([IZHIKEVICH_RS["d"]]),
    )
    assert float(rs_node.a[0]) == pytest.approx(0.02)
    assert float(rs_node.b[0]) == pytest.approx(0.20)
    assert float(rs_node.c[0]) == pytest.approx(-65.0)
    assert float(rs_node.d[0]) == pytest.approx(8.0)

    fs_node = Izhikevich(
        a=np.array([IZHIKEVICH_FS["a"]]),
        b=np.array([IZHIKEVICH_FS["b"]]),
        c=np.array([IZHIKEVICH_FS["c"]]),
        d=np.array([IZHIKEVICH_FS["d"]]),
    )
    assert float(fs_node.a[0]) == pytest.approx(0.10)
    assert float(fs_node.b[0]) == pytest.approx(0.20)
    assert float(fs_node.c[0]) == pytest.approx(-65.0)
    assert float(fs_node.d[0]) == pytest.approx(2.0)


# =========================================================================
# 2. Dale's Principle Enforcement
# =========================================================================

def test_dales_principle_valid_matrices():
    """Verify that purely excitatory or purely inhibitory presynaptic columns pass."""
    # Presynaptic neuron 0: excitatory (all >= 0)
    # Presynaptic neuron 1: inhibitory (all <= 0)
    w_valid = np.array([
        [10.0, -5.0],
        [20.0, -15.0],
        [0.0,   0.0],
    ], dtype=np.float32)

    assert validate_dales_principle(w_valid) is True
    enforce_dales_principle(w_valid)  # Should not raise


def test_dales_principle_violation_raises():
    """Verify that a presynaptic neuron with mixed positive and negative outgoing weights raises error."""
    # Presynaptic neuron 0 has both positive and negative projections
    w_invalid = np.array([
        [10.0, -5.0],
        [-5.0, -10.0],
    ], dtype=np.float32)

    assert validate_dales_principle(w_invalid) is False
    with pytest.raises(DalesPrincipleError):
        enforce_dales_principle(w_invalid)


def test_decompose_to_dales_principle():
    """Verify decomposition of signed matrix into Dale-compliant excitatory and inhibitory sub-matrices."""
    w_mixed = np.array([
        [10.0, -5.0],
        [-8.0, 12.0],
    ], dtype=np.float32)

    w_exc, w_inh = decompose_to_dales_principle(w_mixed)
    assert np.all(w_exc >= 0.0)
    assert np.all(w_inh <= 0.0)
    assert np.allclose(w_exc + w_inh, w_mixed)


# =========================================================================
# 3. Topological Sort & Recurrence Detection
# =========================================================================

def test_feedforward_topological_sort():
    """Verify Kahn's topological sort on multi-layer feedforward graph."""
    graph = NIRGraph()
    graph.add_node("input", Input(input_type={"input": (4,)}))
    graph.add_node("lin1", Linear(weight=np.zeros((8, 4), dtype=np.float32)))
    graph.add_node("lif1", CubaLIF())
    graph.add_node("lin2", Linear(weight=np.zeros((2, 8), dtype=np.float32)))
    graph.add_node("output", Output(output_type={"output": (2,)}))

    graph.add_edge("input", "lin1")
    graph.add_edge("lin1", "lif1")
    graph.add_edge("lif1", "lin2")
    graph.add_edge("lin2", "output")

    assert graph.is_recurrent() is False
    order = graph.topological_sort()
    assert order == ["input", "lin1", "lif1", "lin2", "output"]


def test_recurrent_graph_detection():
    """Verify cycle detection in recurrent neuromorphic graph."""
    graph = NIRGraph()
    graph.add_node("input", Input(input_type={"input": (4,)}))
    graph.add_node("lin1", Linear(weight=np.zeros((4, 4), dtype=np.float32)))
    graph.add_node("lif1", CubaLIF())
    graph.add_node("lin_rec", Linear(weight=np.zeros((4, 4), dtype=np.float32)))
    graph.add_node("output", Output(output_type={"output": (4,)}))

    graph.add_edge("input", "lin1")
    graph.add_edge("lin1", "lif1")
    graph.add_edge("lif1", "lin_rec")
    graph.add_edge("lin_rec", "lif1")  # Recurrent cycle
    graph.add_edge("lif1", "output")

    assert graph.is_recurrent() is True
    order = graph.topological_sort()
    assert len(order) == 5
    assert set(order) == {"input", "lin1", "lif1", "lin_rec", "output"}


# =========================================================================
# 4. HDF5 and JSON Round-Trip Serialization
# =========================================================================

def test_hdf5_serialization_roundtrip():
    """Verify saving and loading NIRGraph with HDF5 .nir format."""
    graph = NIRGraph()
    graph.add_node("input", Input(input_type={"input": (2,)}))
    graph.add_node("linear", Linear(weight=np.array([[5.0, 10.0], [15.0, 20.0]], dtype=np.float32)))
    graph.add_node(
        "cubalif",
        CubaLIF(
            tau_mem=np.array([20.0, 20.0], dtype=np.float32),
            tau_syn=np.array([5.0, 5.0], dtype=np.float32),
            v_leak=np.array([-70.0, -70.0], dtype=np.float32),
            v_threshold=np.array([-50.0, -50.0], dtype=np.float32),
            v_reset=np.array([-75.0, -75.0], dtype=np.float32),
        )
    )
    graph.add_node("output", Output(output_type={"output": (2,)}))
    graph.add_edge("input", "linear")
    graph.add_edge("linear", "cubalif")
    graph.add_edge("cubalif", "output")

    with tempfile.NamedTemporaryFile(suffix=".nir", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        save_nir_hdf5(graph, tmp_path)
        loaded = load_nir_hdf5(tmp_path)

        assert loaded.version == "1.0.0"
        assert set(loaded.nodes.keys()) == {"input", "linear", "cubalif", "output"}
        assert len(loaded.edges) == 3

        # Check node types
        assert isinstance(loaded.nodes["input"], Input)
        assert isinstance(loaded.nodes["linear"], Linear)
        assert isinstance(loaded.nodes["cubalif"], CubaLIF)
        assert isinstance(loaded.nodes["output"], Output)

        # Check numerical weights
        np.testing.assert_allclose(loaded.nodes["linear"].weight, graph.nodes["linear"].weight)
        np.testing.assert_allclose(loaded.nodes["cubalif"].tau_mem, graph.nodes["cubalif"].tau_mem)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def test_json_serialization_roundtrip():
    """Verify saving and loading NIRGraph with JSON schema."""
    graph = NIRGraph()
    graph.add_node("input", Input(input_type={"input": (3,)}))
    graph.add_node("affine", Affine(
        weight=np.array([[1.0, 2.0, 3.0]], dtype=np.float32),
        bias=np.array([0.5], dtype=np.float32)
    ))
    graph.add_node("output", Output(output_type={"output": (1,)}))
    graph.add_edge("input", "affine")
    graph.add_edge("affine", "output")

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        save_nir_json(graph, tmp_path)
        loaded = load_nir_json(tmp_path)

        assert set(loaded.nodes.keys()) == {"input", "affine", "output"}
        assert len(loaded.edges) == 2
        np.testing.assert_allclose(loaded.nodes["affine"].weight, graph.nodes["affine"].weight)
        np.testing.assert_allclose(loaded.nodes["affine"].bias, graph.nodes["affine"].bias)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


# =========================================================================
# 5. Ingestion Pipeline: NIR -> WetLang Source, AST, WBC & C99 VM Execution
# =========================================================================

def test_nir_to_wet_source_generation():
    """Verify emission of valid WetLang source from NIR graph."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (2,)}))
    graph.add_node("w", Linear(weight=np.array([[10.0, 15.0], [5.0, 8.0]], dtype=np.float32)))
    graph.add_node("out", Output(output_type={"output": (2,)}))
    graph.add_edge("in", "w")
    graph.add_edge("w", "out")

    src = nir_to_wet_source(graph, mea_rows=8, mea_cols=8, num_cycles=50)
    assert "grid mea[8, 8];" in src
    assert "channel stim_0 = mea[0, 0] mode: BiphasicStim;" in src
    assert "channel stim_1 = mea[0, 1] mode: BiphasicStim;" in src
    assert "channel sense_0" in src
    assert "while (tick_counter < 50)" in src
    assert "sync_tick();" in src


def test_nir_to_wet_ast():
    """Verify emission of ProgramNode AST from NIR graph."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (1,)}))
    graph.add_node("out", Output(output_type={"output": (1,)}))
    graph.add_edge("in", "out")

    ast = nir_to_wet_ast(graph)
    assert isinstance(ast, ProgramNode)
    assert len(ast.declarations) > 0


def test_nir_to_wet_bytecode_and_native_execution():
    """Verify full end-to-end pipeline: NIR -> .wbc bytecode -> C99 VM execution."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (2,)}))
    graph.add_node("linear", Linear(weight=np.array([[12.0, 8.0], [6.0, 10.0]], dtype=np.float32)))
    graph.add_node("out", Output(output_type={"output": (2,)}))
    graph.add_edge("in", "linear")
    graph.add_edge("linear", "out")

    # 1. Compile directly to .wbc bytecode
    bytecode = nir_to_wet_bytecode(graph, num_cycles=25)
    assert len(bytecode) > 32
    assert bytecode[:4] == HEADER_MAGIC

    # 2. Load and execute in C99 Native VM
    with WetRuntime() as rt:
        rt.load(bytecode)
        rt.step(25)
        assert rt.current_tick == 25
        assert rt.sim_time_ms == pytest.approx(2.5, abs=0.01)

        # Telemetry should be active
        telem = rt.get_telemetry()
        assert telem.current_tick == 25
        assert len(telem.channel_voltages) == 64


def test_nir_dimension_validation_exceeding_channels():
    """Verify NIRValidationError is raised when NIR graph requires more than 64 channels."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (50,)}))
    graph.add_node("out", Output(output_type={"output": (20,)}))  # 50 + 20 = 70 > 64
    graph.add_edge("in", "out")

    with pytest.raises(NIRValidationError):
        nir_to_wet_source(graph, mea_rows=8, mea_cols=8)


# =========================================================================
# 6. Export Pipeline: WetLang AST, WBC & Live VM -> NIRGraph
# =========================================================================

def test_wet_ast_to_nir():
    """Verify conversion from WetLang AST to standard NIRGraph."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (2,)}))
    graph.add_node("out", Output(output_type={"output": (2,)}))
    graph.add_edge("in", "out")

    ast = nir_to_wet_ast(graph)
    exported = wet_ast_to_nir(ast)

    assert "input" in exported.nodes
    assert "synapses" in exported.nodes
    assert "lif_layer" in exported.nodes
    assert "output" in exported.nodes
    assert len(exported.edges) == 3


def test_wet_bytecode_to_nir():
    """Verify parsing compiled .wbc bytecode back into standard NIRGraph."""
    graph = NIRGraph()
    graph.add_node("in", Input(input_type={"input": (2,)}))
    graph.add_node("out", Output(output_type={"output": (2,)}))
    graph.add_edge("in", "out")

    bytecode = nir_to_wet_bytecode(graph)
    exported = wet_bytecode_to_nir(bytecode)

    assert "input" in exported.nodes
    assert "weight" in exported.nodes
    assert "lif" in exported.nodes
    assert "output" in exported.nodes


def test_wet_vm_to_nir():
    """Verify live VM introspection export to standard NIRGraph."""
    with WetRuntime() as rt:
        exported = wet_vm_to_nir(rt, num_neurons=64)
        assert "input" in exported.nodes
        assert "synaptic_matrix" in exported.nodes
        assert "organoid_neurons" in exported.nodes
        assert "output" in exported.nodes

        syn_weight = exported.nodes["synaptic_matrix"].weight
        assert syn_weight.shape == (64, 64)
        assert np.all(syn_weight >= 0.0)
        assert np.all(syn_weight <= 40.0)


def test_vm_get_synapse_matrix_live():
    """Verify get_synapse_matrix extracts genuine 64x64 biophysics conductance matrix."""
    with WetRuntime() as rt:
        mat = rt.get_synapse_matrix()
        assert isinstance(mat, np.ndarray)
        assert mat.shape == (64, 64)
        assert mat.dtype == np.float32
        assert np.all(mat >= 0.0)
        assert np.all(mat <= 40.0)

        # Query individual weights
        w01 = rt.get_synapse_weight(0, 1)
        assert isinstance(w01, float)
        assert 0.0 <= w01 <= 40.0


# =========================================================================
# 7. Multi-Layer and Advanced Round-Trip Verification
# =========================================================================

def test_multilayer_feedforward_pipeline():
    """Verify multi-layer feedforward network ingestion and bytecode synthesis."""
    graph = NIRGraph()
    # Layer 1: 4 inputs -> 8 hidden neurons
    graph.add_node("in", Input(input_type={"input": (4,)}))
    w1 = np.ones((8, 4), dtype=np.float32) * 5.0
    graph.add_node("fc1", Linear(weight=w1))
    graph.add_node("lif1", CubaLIF())

    # Layer 2: 8 hidden -> 2 outputs
    w2 = np.ones((2, 8), dtype=np.float32) * 8.0
    graph.add_node("fc2", Linear(weight=w2))
    graph.add_node("lif2", CubaLIF())
    graph.add_node("out", Output(output_type={"output": (2,)}))

    graph.add_edge("in", "fc1")
    graph.add_edge("fc1", "lif1")
    graph.add_edge("lif1", "fc2")
    graph.add_edge("fc2", "lif2")
    graph.add_edge("lif2", "out")

    # Ingest to bytecode and run
    bytecode = nir_to_wet_bytecode(graph, num_cycles=20)
    with WetRuntime() as rt:
        rt.load(bytecode)
        rt.step(20)
        assert rt.current_tick == 20


def test_hdf5_to_bytecode_roundtrip():
    """Verify saving to HDF5, reloading, and compiling to bytecode."""
    graph = NIRGraph()
    graph.add_node("input", Input(input_type={"input": (3,)}))
    w = np.array([
        [10.0, 5.0, 2.0],
        [4.0, 12.0, 8.0],
        [1.0, 3.0, 15.0],
    ], dtype=np.float32)
    graph.add_node("syn", Linear(weight=w))
    graph.add_node("neurons", CubaLIF())
    graph.add_node("output", Output(output_type={"output": (3,)}))
    graph.add_edge("input", "syn")
    graph.add_edge("syn", "neurons")
    graph.add_edge("neurons", "output")

    with tempfile.NamedTemporaryFile(suffix=".nir", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        save_nir_hdf5(graph, tmp_path)
        reloaded = load_nir_hdf5(tmp_path)
        bc = nir_to_wet_bytecode(reloaded, num_cycles=10)
        assert len(bc) > 32
        assert bc[:4] == HEADER_MAGIC
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def test_affine_dales_principle():
    """Verify Dale's principle enforcement on Affine layers (weight + bias)."""
    # Affine with Dale-compliant weights
    w_good = np.array([[5.0, -10.0], [8.0, -12.0]], dtype=np.float32)
    b = np.array([0.1, 0.2], dtype=np.float32)
    aff_good = Affine(weight=w_good, bias=b)
    enforce_dales_principle(aff_good.weight)

    # Affine with Dale-violating weights
    w_bad = np.array([[5.0, -10.0], [-8.0, -12.0]], dtype=np.float32)
    aff_bad = Affine(weight=w_bad, bias=b)
    with pytest.raises(DalesPrincipleError):
        enforce_dales_principle(aff_bad.weight)

