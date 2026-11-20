def f(x):
    return x**3 - 4.0 * x - 9.0

def df(x):
    return 3.0 * x**2 - 4.0

def newton_method(func, dfunc, x0, tol=1e-9, max_iter=100):
    x = x0
    for k in range(1, max_iter + 1):
        deriv = dfunc(x)
        if deriv == 0:
            raise ZeroDivisionError("Derivative hit zero during Newton step")
        x_next = x - func(x) / deriv
        if abs(x_next - x) < tol:
            return x_next, k
        x = x_next
    return x, max_iter

def secant_method(func, x0, x1, tol=1e-9, max_iter=100):
    for k in range(1, max_iter + 1):
        denom = func(x1) - func(x0)
        if denom == 0:
            raise ZeroDivisionError("Zero denominator in secant step")
        x2 = x1 - func(x1) * (x1 - x0) / denom
        if abs(x2 - x1) < tol:
            return x2, k
        x0, x1 = x1, x2
    return x1, max_iter

root_newton, iter_newton = newton_method(f, df, 3.0)
root_secant, iter_secant = secant_method(f, 2.0, 3.0)

print("Newton root:", round(root_newton, 9), "in", iter_newton, "iters")
print("Secant root:", round(root_secant, 9), "in", iter_secant, "iters")
