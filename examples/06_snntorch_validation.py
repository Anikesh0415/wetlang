"""
Example 06: Columbia University snnTorch Cross-Framework Biophysical Validation
Mathematically benchmarks Wetworld Exact Exponential Euler ODE against PyTorch snnTorch LIF.
"""

from wetlang.sandbox.snntorch_cross_validation import run_snntorch_cross_validation


def main():
    print("Running snnTorch Cross-Validation against Wetworld C99 Engine...")
    results = run_snntorch_cross_validation(steps=60, dt_ms=0.1)

    print("\nQuantitative Convergence Metrics:")
    print(f"  Membrane Time Constant (tau_m) : {results['tau_m_ms']:.1f} ms")
    print(f"  Discrete Decay Factor (beta)   : {results['beta_decay_factor']:.6f}")
    print(f"  Decay Root Mean Square Error   : {results['decay_rmse']:.6f}")
    print(f"  Pearson Correlation (r)        : {results['pearson_correlation']:.12f}")
    print(f"  snnTorch Library Version       : {results['snntorch_version']}")
    print(f"  Validation Status              : {'PASSED (r > 0.999)' if results['validation_passed'] else 'FAILED'}")


if __name__ == "__main__":
    main()
