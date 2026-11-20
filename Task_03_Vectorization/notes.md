# Task 3: Vectorization vs. Python Loops

## Input Values and Mathematical Operations
- **Input:** A sequence of `1,000,000` numeric values (`0` to `999,999`) represented as a Python list for the loop benchmark and as a `float64` NumPy array (`np.arange`) for the vectorized version.
- **Operations:** Element-wise affine transformation `y = 2.5 * x + 10.0`, timing measurements via `time.perf_counter`, speedup ratio (`loop_time / vec_time`), and maximum absolute difference (`np.max(np.abs(...))`).

## Parameter Change ("What-If")
- Increasing `n` from `1,000,000` to `10,000,000` increases execution time for both paths, but the Python loop scales much more slowly because every iteration incurs Python bytecode and type-checking overhead, whereas NumPy executes contiguous C/SIMD loops over `ndarray` buffers.

## Meaning of Output
- Prints the elapsed wall-clock time for both the Python loop and the vectorized NumPy expression, the relative speedup multiplier, and the maximum numerical difference between the two outputs (which should be near `0.0` / floating-point machine precision).

## Modified Real-World Case: Sensor Signal Calibration (`mV` to `V`)
- **Assumptions:** `500,000` raw millivolt (`mV`) telemetry/sensor readings share a `100.0 mV` baseline offset and require conversion to volts (`V`) via `(mv - 100.0) / 1000.0`.
- **Input Data:** `500,000` periodic signal samples generated from `120.0 + (i % 250) * 0.4`.
- **Output:** Reports loop vs. vectorized runtime, speedup factor, mean calibrated voltage (`V`), and peak calibrated voltage (`V`).
- **Interpretation:** Vectorization produces identical calibrated voltages far faster than list comprehension loops, making batch telemetry and signal preprocessing practical on larger datasets.
