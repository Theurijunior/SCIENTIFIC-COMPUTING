import numpy as np

# Monte Carlo simulation to estimate pi using random points in [-1, 1]^2
rng = np.random.default_rng(seed=42)
n_samples = 200_000

x = rng.uniform(-1.0, 1.0, size=n_samples)
y = rng.uniform(-1.0, 1.0, size=n_samples)

inside_circle = (x**2 + y**2) <= 1.0
pi_estimate = 4.0 * np.mean(inside_circle)
abs_error = abs(pi_estimate - np.pi)
std_error = 4.0 * np.sqrt(np.mean(inside_circle) * (1.0 - np.mean(inside_circle)) / n_samples)

print(f"Samples: {n_samples}")
print(f"Estimated pi: {pi_estimate:.6f}")
print(f"Absolute error: {abs_error:.6f}")
print(f"Standard error: {std_error:.6f}")
