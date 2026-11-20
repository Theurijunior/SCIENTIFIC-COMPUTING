import numpy as np
from scipy.optimize import fsolve, root

# System of two nonlinear equations:
# f1(x, y) = x^2 + y^2 - 25 = 0
# f2(x, y) = x - y - 1 = 0

def system_eqs(vars_vec):
    x, y = vars_vec
    return [
        x**2 + y**2 - 25.0,
        x - y - 1.0
    ]

def jacobian_eqs(vars_vec):
    x, y = vars_vec
    return np.array([
        [2.0 * x, 2.0 * y],
        [1.0, -1.0]
    ], dtype=float)

guess = np.array([3.0, 2.0])
sol_fsolve = fsolve(system_eqs, guess, fprime=jacobian_eqs)
sol_root = root(system_eqs, guess, jac=jacobian_eqs, method="hybr")

print("fsolve solution (x, y):", np.round(sol_fsolve, 8))
print("root(hybr) solution (x, y):", np.round(sol_root.x, 8))
print("Residual norm:", np.linalg.norm(system_eqs(sol_root.x)))
