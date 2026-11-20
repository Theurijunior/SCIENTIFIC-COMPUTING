# Task 2: NumPy Arrays and Numerical Computation

## Input Values and Mathematical Operations
- **Input:** A 1D NumPy array of 24 hourly temperature readings in degrees Celsius (`17.5` °C to `29.4` °C).
- **Operations:** Arithmetic mean (`np.mean`), minimum (`np.min`), maximum (`np.max`), and vectorized linear unit conversion `F = 1.8 * C + 32` applied across the full array without a Python loop.

## Parameter Change ("What-If")
- Increasing the afternoon peak readings (`28.3`–`29.4` °C) by `+3.0` °C raises both the daily mean and the maximum temperature, while the minimum (`17.5` °C) stays unchanged unless early-morning readings are also adjusted.

## Meaning of Output
- Prints the daily mean, minimum, and maximum temperatures in Celsius and slices the first six converted Fahrenheit temperatures (`temperatures_f[:6]`) to confirm the element-wise conversion works as intended.

## Modified Real-World Case: Router Interface Throughput
- **Assumptions:** A network interface records 12 two-hour average throughput values in megabits per second (Mbps), and dividing by `8.0` converts bit-rate throughput into megabytes per second (MB/s).
- **Input Data:** Twelve 2-hour throughput samples ranging from `28.0` Mbps to `160.8` Mbps.
- **Output:** Displays the average, lowest, and peak throughput in Mbps along with the first six values converted to MB/s (rounded to two decimal places).
- **Interpretation:** Captures off-peak versus peak traffic windows on the link and gives byte-rate equivalents useful for estimating transfer or logging capacity.# Task_02_NumPy_Arrays
