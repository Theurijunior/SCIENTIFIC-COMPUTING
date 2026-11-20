import numpy as np

# Solve a linear system Ax = b using NumPy's linear algebra solver
A = np.array([
    [3.0, 2.0, -1.0],
    [2.0, -2.0, 4.0],
    [-1.0, 0.5, -1.0]
])

b = np.array([1.0, -2.0, 0.0])

# Solve Ax = b directly (preferred over inv(A) @ b for stability and speed)
x = np.linalg.solve(A, b)

# Verify residual ||Ax - b||
residual = np.linalg.norm(A @ x - b, ord=2)

print("Coefficient matrix A:\n", A)
print("\nRight-hand side vector b:\n", b)
print("\nSolution vector x:\n", x)
print(f"\nResidual norm ||Ax - b||_2: {residual:.2e}")
