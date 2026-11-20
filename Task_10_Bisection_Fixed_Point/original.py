import math

def f(x):
    return x**3 - x - 2.0

def g(x):
    return (x + 2.0)**(1.0 / 3.0)

def bisection(func, a, b, tol=1e-8, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Bracket must have opposite signs at endpoints")
    for k in range(1, max_iter + 1):
        mid = 0.5 * (a + b)
        if abs(func(mid)) < tol or 0.5 * (b - a) < tol:
            return mid, k
        if func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
    return 0.5 * (a + b), max_iter

def fixed_point(func_g, x0, tol=1e-8, max_iter=100):
    x = x0
    for k in range(1, max_iter + 1):
        x_next = func_g(x)
        if abs(x_next - x) < tol:
            return x_next, k
        x = x_next
    return x, max_iter

root_bisect, iter_bisect = bisection(f, 1.0, 2.0)
root_fp, iter_fp = fixed_point(g, 1.5)

print("Bisection root:", round(root_bisect, 8), "in", iter_bisect, "iters")
print("Fixed-point root:", round(root_fp, 8), "in", iter_fp, "iters")
