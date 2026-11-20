import numpy as np
from scipy.optimize import minimize

def objective(x):
    return (x[0] - 2.0)**2 + 3.0 * (x[1] + 1.5)**2 + np.sin(x[0])

def grad_objective(x):
    return np.array([
        2.0 * (x[0] - 2.0) + np.cos(x[0]),
        6.0 * (x[1] + 1.5)
    ])

x0 = np.array([0.0, 0.0])
res_bfgs = minimize(objective, x0, jac=grad_objective, method="BFGS")

# Simple gradient descent check
lr = 0.05
x_gd = x0.copy()
for _ in range(300):
    x_gd = x_gd - lr * grad_objective(x_gd)

print("BFGS minimum point:", np.round(res_bfgs.x, 6))
print("BFGS objective value:", round(res_bfgs.fun, 6))
print("Gradient descent point:", np.round(x_gd, 6))
