import numpy as np

# Real-world case: total energy (kWh) consumed over a 24-hour window
# from hourly power draw samples (kW) using the trapezoidal rule

hours = np.arange(0.0, 25.0, 1.0)
power_kw = np.array([
    1.2, 1.0, 0.9, 0.9, 1.1, 1.6, 2.5, 3.4,
    3.8, 3.2, 2.9, 2.7, 3.1, 2.8, 2.6, 2.9,
    3.6, 4.5, 5.2, 4.9, 3.8, 2.7, 1.9, 1.4, 1.2
])

energy_kwh = np.trapezoid(power_kw, hours) if hasattr(np, "trapezoid") else np.trapz(power_kw, hours)
avg_power_kw = energy_kwh / (hours[-1] - hours[0])

print(f"Total 24-hour energy consumption: {energy_kwh:.2f} kWh")
print(f"Average power draw over 24 hours: {avg_power_kw:.2f} kW")
