import numpy as np

# Real-world case: cooling of a server or electronic component toward ambient room temperature
# Newton's law of cooling: dT/dt = -k * (T - T_ambient)

k_cool = 0.15
t_ambient = 24.0
t_init = 78.0
duration_min = 30.0
steps = 60

dt = duration_min / steps
times = np.linspace(0.0, duration_min, steps + 1)
temps = np.zeros(steps + 1)
temps[0] = t_init

for i in range(steps):
    dtemp = -k_cool * (temps[i] - t_ambient)
    temps[i + 1] = temps[i] + dt * dtemp

for idx in [0, 10, 20, 40, 60]:
    print(f"t={times[idx]:4.1f} min -> temp={temps[idx]:5.2f} C")
