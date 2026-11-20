import numpy as np

# Demonstrate catastrophic cancellation and floating-point rounding error
# Evaluate f(x) = sqrt(x^2 + 1) - 1 for small x using direct vs. rationalized form

x_vals = np.array([1e-1, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12])

# Direct evaluation (suffers from cancellation when x^2 << 1)
direct = np.sqrt(x_vals**2 + 1.0) - 1.0

# Numerically stable equivalent: x^2 / (sqrt(x^2 + 1) + 1)
stable = (x_vals**2) / (np.sqrt(x_vals**2 + 1.0) + 1.0)

print(f"{'x':>12} | {'Direct':>18} | {'Stable':>18} | {'Abs Diff':>12}")
print("-" * 68)
for x, d, s in zip(x_vals, direct, stable):
    diff = abs(d - s)
    print(f"{x:12.1e} | {d:18.12e} | {s:18.12e} | {diff:12.2e}")
