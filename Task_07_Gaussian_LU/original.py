import numpy as np
from scipy.linalg import lu

A = np.array([
    [2.0, 1.0, 1.0],
    [4.0, -6.0, 0.0],
    [-2.0, 7.0, 2.0]
])
b = np.array([5.0, -2.0, 9.0])

def gaussian_elimination(M, rhs):
    M = M.astype(float).copy()
    rhs = rhs.astype(float).copy()
    n = len(rhs)

    for col in range(n):
        pivot = col + np.argmax(np.abs(M[col:, col]))
        M[[col, pivot]] = M[[pivot, col]]
        rhs[[col, pivot]] = rhs[[pivot, col]]

        for row in range(col + 1, n):
            factor = M[row, col] / M[col, col]
            M[row, col:] = M[row, col:] - factor * M[col, col:]
            rhs[row] = rhs[row] - factor * rhs[col]

    x = np.zeros(n)
    for row in range(n - 1, -1, -1):
        x[row] = (rhs[row] - np.dot(M[row, row + 1:], x[row + 1:])) / M[row, row]
    return x

x_gauss = gaussian_elimination(A, b)
P, L, U = lu(A)
x_lu = np.linalg.solve(A, b)

print("Gaussian elimination solution:", np.round(x_gauss, 6))
print("LU solve solution:", np.round(x_lu, 6))
print("Lower triangular matrix L:\n", np.round(L, 4))
print("Upper triangular matrix U:\n", np.round(U, 4))
