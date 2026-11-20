import time
import numpy as np

# Real-world scenario: converting raw packet/sensor signal readings (in mV)
# into calibrated engineering units (e.g., voltage drop in V with baseline offset)
# across 500,000 samples

n_samples = 500_000
raw_mv = [120.0 + (i % 250) * 0.4 for i in range(n_samples)]

# Baseline approach using a Python loop
t0 = time.perf_counter()
loop_volts = [(mv - 100.0) / 1000.0 for mv in raw_mv]
t_loop = time.perf_counter() - t0

# Vectorized NumPy approach
arr_mv = np.array(raw_mv, dtype=np.float64)
t1 = time.perf_counter()
vec_volts = (arr_mv - 100.0) / 1000.0
t_vec = time.perf_counter() - t1

mean_volts = np.mean(vec_volts)
peak_volts = np.max(vec_volts)
speedup = t_loop / t_vec

print(f"Loop calibration time: {t_loop:.6f} s")
print(f"Vectorized calibration time: {t_vec:.6f} s")
print(f"Speedup: {speedup:.2f}x")
print(f"Mean calibrated signal: {mean_volts:.4f} V")
print(f"Peak calibrated signal: {peak_volts:.4f} V")
