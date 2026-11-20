import numpy as np
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2)

def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def simpsons_rule(func, a, b, n):
    if n % 2 != 0:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = func(x)
    h = (b - a) / n
    return (h / 3.0) * (y[0] + 4.0 * np.sum(y[1:-1:2]) + 2.0 * np.sum(y[2:-2:2]) + y[-1])

a, b = 0.0, 2.0
exact_quad, _ = quad(f, a, b)

for n in [10, 20, 50, 100]:
    t_val = trapezoidal_rule(f, a, b, n)
    s_val = simpsons_rule(f, a, b, n)
    print(f"n={n:3d} | trap_err={abs(t_val - exact_quad):.2e} | simp_err={abs(s_val - exact_quad):.2e}")
