import numpy as np

# Real-world case: estimating instantaneous acceleration (m/s^2)
# from vehicle position samples s(t) (meters) over time t (seconds)

t = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
s = np.array([0.0, 2.1, 8.4, 18.9, 33.6, 52.5, 75.6])

dt = t[1] - t[0]
velocity = np.gradient(s, dt)
acceleration = np.gradient(velocity, dt)

for ti, si, vi, ai in zip(t, s, velocity, acceleration):
    print(f"t={ti:3.1f}s | pos={si:5.1f}m | vel={vi:5.2f}m/s | acc={ai:5.2f}m/s^2")
