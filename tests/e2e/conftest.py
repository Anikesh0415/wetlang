"""Pytest configuration and marker registration for WetLang v2.2 E2E tests.

Strictly avoids importing wetlang, bindings, compiler, tests.e2e.common, or
loading wetvm.dll at import/collection time.
"""

import pytest


def pytest_configure(config: pytest.Config) -> None:
    markers = [
        "m1: Milestone M1 (Native C99 VM, Closed-Loop Hooks & OS Transports)",
        "m2: Milestone M2 (Language, VS Code Grammar, Semantic Safety & SET_BLANKING Compiler)",
        "m3: Milestone M3 (NWB 2.x Engine, CLI nwb & LSL Adapter)",
        "m4: Milestone M4 (Multi-Backend Targets & Biophysics Validation)",
        "m5: Milestone M5 (NWB Benchmarks, Release Hygiene & Version 2.2.0)",
        "tier1: Tier 1 Category-Partition happy-path E2E tests",
        "tier2: Tier 2 Boundary Value Analysis and negative fault-injection E2E tests",
        "tier3: Tier 3 Cross-feature pairwise integration E2E tests",
        "tier4: Tier 4 Real-world application workload E2E tests",
    ]
    for marker in markers:
        config.addinivalue_line("markers", marker)
