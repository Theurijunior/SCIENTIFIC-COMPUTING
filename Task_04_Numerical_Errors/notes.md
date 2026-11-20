# Task 4: Numerical Errors and Floating-Point Precision

## Input Values and Mathematical Operations
- **Input:** Small positive values `x` (`1e-1` down to `1e-12`) passed into `f(x) = sqrt(x^2 + 1) - 1`.
- **Operations:** Direct evaluation `np.sqrt(x**2 + 1.0) - 1.0` versus algebraically equivalent rationalization `(x**2) / (np.sqrt(x**2 + 1.0) + 1.0)`, followed by absolute difference comparison.

## Parameter Change ("What-If")
- Pushing `x` even smaller (such as `1e-16`) causes `x**2 + 1.0` to round to `1.0` in IEEE-754 `float64` (~15–17 decimal digits of precision), making the direct subtraction `1.0 - 1.0 = 0.0` while the rationalized form preserves accuracy.

## Meaning of Output
- Prints a side-by-side table of `x`, the direct result, the stabilized result, and the absolute difference so you can see precision degrade as `x` shrinks and `sqrt(x^2 + 1)` approaches `1.0`.

## Modified Real-World Case: Baseline vs. Small Delta Subtraction
- **Assumptions:** A large baseline metric (`1e9`, such as a 1-billion-unit quota or byte count) is combined with smaller deltas (`1e5` down to `1e-8`) using IEEE-754 `float64` arithmetic.
- **Input Data:** Baseline `1e9` and delta values `[1e5, 1e3, 1.0, 1e-1, 1e-6, 1e-8]`.
- **Output:** Displays `(baseline + delta) - baseline`, the expected delta, and the relative error percentage for each case.
- **Interpretation:** Subtracting nearly equal numbers after adding a tiny increment to a large baseline can wipe out significant digits—showing why tracking deltas directly or reformulating expressions matters in numerical code.
