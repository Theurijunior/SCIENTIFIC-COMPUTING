import numpy as np

# Matrix algebra fundamentals: transpose, matrix product, determinant, and inverse
A = np.array([
    [4.0, 2.0, 1.0],
    [1.0, 3.0, 2.0],
    [2.0, 1.0, 5.0]
])

B = np.array([
    [1.0, 0.0, 2.0],
    [3.0, 1.0, 0.0],
    [0.0, 2.0, 1.0]
])

A_T = A.T
AB = A @ B
BA = B @ A
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
identity_check = A @ inv_A

print("Matrix A:\n", A)
print("\nTranspose of A (A.T):\n", A_T)
print("\nProduct A @ B:\n", AB)
print("\nProduct B @ A (non-commutative check):\n", BA)
print(f"\nDeterminant of A: {det_A:.4f}")
print("\nInverse of A:\n", inv_A)
print("\nCheck A @ inv(A) ~ I:\n", np.round(identity_check, 6))
