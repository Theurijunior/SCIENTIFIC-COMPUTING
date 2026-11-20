import numpy as np

# Real-world scenario: computing relative capacity change when a small
# overhead/jitter margin (delta) is added to a large baseline bandwidth/storage value
# Naive subtraction: (baseline + delta) - baseline
# Stabilized subtraction: ((baseline + delta) - baseline) vs explicit delta check

baseline = 1e9          # e.g., 1,000,000,000 bytes (1 GB baseline allocation)
deltas = np.array([1e5, 1e3, 1.0, 1e-1, 1e-6, 1e-8])

naive_delta = (baseline + deltas) - baseline
relative_error = np.abs(naive_delta - deltas) / deltas

print(f"Baseline: {baseline:.1e}\n")
print(f"{'Delta':>10} | {'(Base+Delta)-Base':>18} | {'True Delta':>12} | {'Rel Error':>10}")
print("-" * 62)
for d, nd, err in zip(deltas, naive_delta, relative_error):
    print(f"{d:10.1e} | {nd:18.8e} | {d:12.4e} | {err:10.2%}")
