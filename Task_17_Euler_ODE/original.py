import numpy as np

def dydt(t, y):
    return -2.0 * y + 1.0

def euler_solve(func, t0, tf, y0, n_steps):
    h = (tf - t0) / n_steps
    t_vals = np.linspace(t0, tf, n_steps + 1)
    y_vals = np.zeros(n_steps + 1)
    y_vals[0] = y0

    for i in range(n_steps):
        y_vals[i + 1] = y_vals[i] + h * func(t_vals[i], y_vals[i])
    return t_vals, y_vals

def exact_sol(t):
    return 0.5 + (0.0 - 0.5) * np.exp(-2.0 * t)

for n in [10, 25, 100]:
    t_grid, y_sim = euler_solve(dydt, 0.0, 2.0, 0.0, n)
    err = abs(y_sim[-1] - exact_sol(2.0))
    print(f"n={n:3d} | y(2.0)={y_sim[-1]:.6f} | abs_err={err:.2e}")
