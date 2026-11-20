import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, y):
    return -0.5 * y + np.sin(2.0 * t)

t_span = (0.0, 6.0)
y0 = [2.0]
t_eval = np.linspace(0.0, 6.0, 13)

def rk4_step(func, t, y, h):
    k1 = func(t, y)
    k2 = func(t + 0.5 * h, y + 0.5 * h * k1)
    k3 = func(t + 0.5 * h, y + 0.5 * h * k2)
    k4 = func(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

def run_rk4(func, t0, tf, y0_val, n_steps):
    h = (tf - t0) / n_steps
    ts = np.linspace(t0, tf, n_steps + 1)
    ys = np.zeros(n_steps + 1)
    ys[0] = y0_val
    for i in range(n_steps):
        ys[i + 1] = rk4_step(func, ts[i], ys[i], h)
    return ts, ys

ts_rk4, ys_rk4 = run_rk4(rhs, 0.0, 6.0, 2.0, 120)
sol_ivp = solve_ivp(rhs, t_span, y0, t_eval=t_eval, method="RK45")

print("RK4 final value at t=6.0:", round(ys_rk4[-1], 6))
print("solve_ivp RK45 final value:", round(sol_ivp.y[0, -1], 6))
print("Max diff at eval points:", np.max(np.abs(ys_rk4[::10] - sol_ivp.y[0])))
