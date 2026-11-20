import numpy as np

A = np.array([
    [10.0, -1.0, 2.0, 0.0],
    [-1.0, 11.0, -1.0, 3.0],
    [2.0, -1.0, 10.0, -1.0],
    [0.0, 3.0, -1.0, 8.0]
])
b = np.array([6.0, 25.0, -11.0, 15.0])

def jacobi(M, rhs, tol=1e-8, max_iter=100):
    n = len(rhs)
    x = np.zeros(n)
    diag = np.diag(M)
    off_diag = M - np.diagflat(diag)

    for k in range(1, max_iter + 1):
        x_new = (rhs - np.dot(off_diag, x)) / diag
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k
        x = x_new
    return x, max_iter

def gauss_seidel(M, rhs, tol=1e-8, max_iter=100):
    n = len(rhs)
    x = np.zeros(n)

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            s1 = np.dot(M[i, :i], x[:i])
            s2 = np.dot(M[i, i + 1:], x_old[i + 1:])
            x[i] = (rhs[i] - s1 - s2) / M[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k
    return x, max_iter

x_j, iter_j = jacobi(A, b)
x_gs, iter_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi solution:", np.round(x_j, 6), "in", iter_j, "iters")
print("Gauss-Seidel solution:", np.round(x_gs, 6), "in", iter_gs, "iters")
print("Direct solve check:", np.round(x_exact, 6))
