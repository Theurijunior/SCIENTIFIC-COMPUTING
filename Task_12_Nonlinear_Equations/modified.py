import numpy as np
from scipy.optimize import root

# Real-world case: two-variable operating point balance where
# x represents active worker nodes and y represents queue buffer size
# eq1: 0.4*x^2 + 1.5*y - 40 = 0
# eq2: 2.0*x - 0.8*y^2 + 3 = 0

def system_balance(state):
    x, y = state
    eq1 = 0.4 * (x**2) + 1.5 * y - 40.0
    eq2 = 2.0 * x - 0.8 * (y**2) + 3.0
    return np.array([eq1, eq2], dtype=float)

init_guess = np.array([6.0, 5.0])
res = root(system_balance, init_guess, method="hybr")

print("Operating point (x, y):", np.round(res.x, 6))
print("Converged:", res.success)
print("Residual check:", np.round(system_balance(res.x), 9))
