import time
import numpy as np

# Compare a Python loop against vectorized NumPy array operations
n = 1_000_000
data = list(range(n))

# Python loop: scale values and apply a linear offset
start_loop = time.perf_counter()
loop_result = [2.5 * x + 10.0 for x in data]
loop_time = time.perf_counter() - start_loop

# Vectorized NumPy computation
arr = np.arange(n, dtype=np.float64)
start_vec = time.perf_counter()
vec_result = 2.5 * arr + 10.0
vec_time = time.perf_counter() - start_vec

max_diff = np.max(np.abs(np.array(loop_result) - vec_result))
speedup = loop_time / vec_time

print(f"Python loop time: {loop_time:.6f} s")
print(f"Vectorized NumPy time: {vec_time:.6f} s")
print(f"Speedup factor: {speedup:.2f}x")
print(f"Max absolute difference: {max_diff:.2e}")
