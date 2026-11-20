import numpy as np

# Real-world case: steady-state node temperatures on a 4-node thermal grid
G = np.array([
    [8.0, -2.0, -2.0, 0.0],
    [-2.0, 8.0, 0.0, -2.0],
    [-2.0, 0.0, 8.0, -2.0],
    [0.0, -2.0, -2.0, 8.0]
])
heat_sources = np.array([120.0, 80.0, 60.0, 40.0])

def gauss_seidel_thermal(M, rhs, tol=1e-7, max_iter=200):
    n = len(rhs)
    temps = np.full(n, 25.0)

    for k in range(1, max_iter + 1):
        prev = temps.copy()
        for i in range(n):
            left = np.dot(M[i, :i], temps[:i])
            right = np.dot(M[i, i + 1:], prev[i + 1:])
            temps[i] = (rhs[i] - left - right) / M[i, i]
        if np.linalg.norm(temps - prev, ord=np.inf) < tol:
            return temps, k
    return temps, max_iter

temps, steps = gauss_seidel_thermal(G, heat_sources)
print("Steady-state node temperatures:", np.round(temps, 4), "in", steps, "steps")
