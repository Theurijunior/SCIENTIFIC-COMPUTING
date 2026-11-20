import numpy as np

A = np.array([
    [4.0, 1.0, 0.0],
    [1.0, 3.0, 1.0],
    [0.0, 1.0, 2.0]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Power iteration for dominant eigenvalue and eigenvector
v = np.array([1.0, 1.0, 1.0])
v = v / np.linalg.norm(v)
lam_prev = 0.0

for _ in range(100):
    w = A @ v
    lam = np.dot(v, w)
    v = w / np.linalg.norm(w)
    if abs(lam - lam_prev) < 1e-10:
        break
    lam_prev = lam

print("All eigenvalues:", np.round(eigenvalues, 6))
print("Eigenvectors:\n", np.round(eigenvectors, 6))
print("Dominant eigenvalue (power iteration):", round(lam, 6))
print("Dominant eigenvector:", np.round(v, 6))
