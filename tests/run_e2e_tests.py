#!/usr/bin/env python3
"""
WetLang E2E Test Suite Runner
Standalone, zero-dependency test runner compatible with Python 3.12+ and pytest.
Supports tier filtering (--tier), feature filtering (--feature), pattern matching (-k),
colorized tabular summary, and automated JSON report generation.
"""

import os
import sys
import time
import json
import unittest
import argparse
from typing import Dict, List, Optional, Set, Any

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class WetLangTestResult(unittest.TextTestResult):
    """
    Custom TestResult tracker that logs per-tier counts (passed, skipped, failed, error)
    and execution timings.
    """

    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.tier_counts: Dict[Any, Dict[str, int]] = {
            1: {"passed": 0, "skipped": 0, "failed": 0, "errors": 0},
            2: {"passed": 0, "skipped": 0, "failed": 0, "errors": 0},
            3: {"passed": 0, "skipped": 0, "failed": 0, "errors": 0},
            4: {"passed": 0, "skipped": 0, "failed": 0, "errors": 0},
            "Infra": {"passed": 0, "skipped": 0, "failed": 0, "errors": 0},
        }
        self.passes: List[Any] = []

    def _get_tier(self, test: Any) -> Any:
        # Check explicit class tier attribute
        if hasattr(test.__class__, "tier"):
            return getattr(test.__class__, "tier")
        # Check module name
        mod = getattr(test.__class__, "__module__", "")
        if "tier1" in mod:
            return 1
        elif "tier2" in mod:
            return 2
        elif "tier3" in mod:
            return 3
        elif "tier4" in mod:
            return 4
        elif "common" in mod:
            return "Infra"
        return 1

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passes.append(test)
        tier = self._get_tier(test)
        if tier not in self.tier_counts:
            self.tier_counts[tier] = {"passed": 0, "skipped": 0, "failed": 0, "errors": 0}
        self.tier_counts[tier]["passed"] += 1

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        tier = self._get_tier(test)
        if tier not in self.tier_counts:
            self.tier_counts[tier] = {"passed": 0, "skipped": 0, "failed": 0, "errors": 0}
        self.tier_counts[tier]["skipped"] += 1

    def addFailure(self, test, err):
        super().addFailure(test, err)
        tier = self._get_tier(test)
        if tier not in self.tier_counts:
            self.tier_counts[tier] = {"passed": 0, "skipped": 0, "failed": 0, "errors": 0}
        self.tier_counts[tier]["failed"] += 1

    def addError(self, test, err):
        super().addError(test, err)
        tier = self._get_tier(test)
        if tier not in self.tier_counts:
            self.tier_counts[tier] = {"passed": 0, "skipped": 0, "failed": 0, "errors": 0}
        self.tier_counts[tier]["errors"] += 1


def filter_suite(
    suite: unittest.TestSuite,
    feature_filter: Optional[List[str]] = None,
    pattern: Optional[str] = None,
) -> unittest.TestSuite:
    """Recursively filter test cases by feature identifier or name/pattern substring."""
    filtered = unittest.TestSuite()
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            filtered.addTests(filter_suite(item, feature_filter, pattern))
        else:
            test_id = item.id()
            doc = getattr(item, "_testMethodDoc", "") or ""
            match = True

            # Substring pattern match
            if pattern and (pattern.lower() not in test_id.lower() and pattern.lower() not in doc.lower()):
                match = False

            # Feature filter match (e.g. F1, F5, F19)
            if feature_filter:
                has_feature = any(
                    f.lower() in test_id.lower() or f.lower() in doc.lower()
                    for f in feature_filter
                )
                if not has_feature:
                    match = False

            if match:
                filtered.addTest(item)
    return filtered


def discover_suite(
    selected_tiers: Optional[List[int]] = None,
    feature_filter: Optional[List[str]] = None,
    pattern: Optional[str] = None,
    include_infra: bool = False,
) -> unittest.TestSuite:
    """Discover test cases matching requested tiers and filters."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    e2e_dir = os.path.join(PROJECT_ROOT, "tests", "e2e")

    tier_files = {
        1: "test_tier1_features.py",
        2: "test_tier2_boundaries.py",
        3: "test_tier3_pairwise.py",
        4: "test_tier4_benchmarks.py",
    }

    tiers_to_load = selected_tiers if selected_tiers else [1, 2, 3, 4]
    found_tier_tests = False

    if os.path.isdir(e2e_dir):
        for tier in tiers_to_load:
            filename = tier_files.get(tier)
            if not filename:
                continue
            filepath = os.path.join(e2e_dir, filename)
            if os.path.isfile(filepath):
                discovered = loader.discover(
                    start_dir=e2e_dir,
                    pattern=filename,
                    top_level_dir=PROJECT_ROOT,
                )
                if discovered.countTestCases() > 0:
                    found_tier_tests = True
                    suite.addTests(discovered)

    # If no tier test files exist yet or include_infra is requested, load common self-tests
    if (not found_tier_tests and not selected_tiers) or include_infra:
        try:
            from tests.e2e.common import TestInfraCommon
            infra_suite = loader.loadTestsFromTestCase(TestInfraCommon)
            suite.addTests(infra_suite)
        except Exception as e:
            print(f"[WARNING] Could not load common infrastructure tests: {e}")

    # Apply filters
    if feature_filter or pattern:
        suite = filter_suite(suite, feature_filter, pattern)

    return suite


def main():
    parser = argparse.ArgumentParser(
        description="WetLang Neural Organoid Platform — 4-Tier E2E Test Suite Runner"
    )
    parser.add_argument(
        "--tier",
        type=str,
        default="",
        help="Comma-separated tier numbers to run (e.g. '1', '1,2', '1,2,3,4')",
    )
    parser.add_argument(
        "--feature",
        type=str,
        default="",
        help="Comma-separated feature IDs to run (e.g. 'F1,F5,F19')",
    )
    parser.add_argument(
        "-k",
        "--pattern",
        type=str,
        default="",
        help="Filter tests by substring pattern in test name or docstring",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose test execution output",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress detailed progress output",
    )
    parser.add_argument(
        "--json-report",
        type=str,
        default="",
        help="Output path for structured JSON test report",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run common infrastructure self-tests (TestInfraCommon)",
    )

    args = parser.parse_args()

    selected_tiers = None
    if args.tier:
        selected_tiers = []
        for part in args.tier.split(","):
            part_s = part.strip()
            if part_s.isdigit():
                selected_tiers.append(int(part_s))

    feature_filter = None
    if args.feature:
        feature_filter = [f.strip() for f in args.feature.split(",") if f.strip()]

    verbosity = 2 if args.verbose else (0 if args.quiet else 1)
    suite = discover_suite(
        selected_tiers=selected_tiers,
        feature_filter=feature_filter,
        pattern=args.pattern,
        include_infra=args.self_test,
    )

    print("=" * 80)
    print(" WetLang Neural Organoid Platform — 4-Tier E2E Test Suite")
    print(f" Python Interpreter : {sys.version.split()[0]} ({sys.executable})")
    print(f" Working Directory  : {PROJECT_ROOT}")
    print(f" Tests Discovered   : {suite.countTestCases()}")
    if selected_tiers:
        print(f" Selected Tiers     : {selected_tiers}")
    if feature_filter:
        print(f" Feature Filter     : {feature_filter}")
    if args.pattern:
        print(f" Pattern Filter     : {args.pattern}")
    print("=" * 80)

    start_time = time.time()
    runner = unittest.TextTestRunner(verbosity=verbosity, resultclass=WetLangTestResult)
    result = runner.run(suite)
    elapsed = time.time() - start_time

    total_passed = len(getattr(result, "passes", []))
    total_skipped = len(result.skipped)
    total_failed = len(result.failures)
    total_errors = len(result.errors)
    total_run = result.testsRun

    print("\n" + "=" * 80)
    print(" E2E Test Execution Summary")
    print("-" * 80)
    print(f"{'Tier':<12}{'Passed':<12}{'Skipped':<12}{'Failed':<12}{'Errors':<12}{'Total':<10}")
    print("-" * 80)

    for tier_key in [1, 2, 3, 4, "Infra"]:
        if tier_key in result.tier_counts:
            tc = result.tier_counts[tier_key]
            tot = tc["passed"] + tc["skipped"] + tc["failed"] + tc["errors"]
            if tot > 0 or tier_key in (1, 2, 3, 4):
                tier_label = f"Tier {tier_key}" if isinstance(tier_key, int) else str(tier_key)
                print(
                    f"{tier_label:<12}"
                    f"{tc['passed']:<12}"
                    f"{tc['skipped']:<12}"
                    f"{tc['failed']:<12}"
                    f"{tc['errors']:<12}"
                    f"{tot:<10}"
                )

    print("-" * 80)
    print(
        f"TOTAL: {total_run} run | {total_passed} passed | {total_skipped} skipped | "
        f"{total_failed} failed | {total_errors} errors"
    )
    print(f"Elapsed Time: {elapsed:.3f} s")
    print("=" * 80)

    if args.json_report:
        report_data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "python_version": sys.version,
            "executable": sys.executable,
            "tests_run": total_run,
            "passed": total_passed,
            "skipped": total_skipped,
            "failures": total_failed,
            "errors": total_errors,
            "elapsed_seconds": elapsed,
            "tiers": result.tier_counts,
            "status": "PASS" if result.wasSuccessful() else "FAIL",
        }
        report_path = os.path.abspath(args.json_report)
        report_dir = os.path.dirname(report_path)
        if report_dir and not os.path.isdir(report_dir):
            os.makedirs(report_dir, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)
        print(f"JSON Test Report saved to: {report_path}")

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
