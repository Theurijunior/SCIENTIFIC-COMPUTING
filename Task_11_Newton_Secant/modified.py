# Real-world case: finding effective interest or growth rate r where
# future value of a recurring deposit reaches a target balance
# Using simplified polynomial approximation f(r) = 1200 * (1 + 6*r + 15*r^2) - 1500 = 0

def balance_gap(r):
    return 1200.0 * (1.0 + 6.0 * r + 15.0 * r**2) - 1500.0

def secant_rate(func, r0, r1, tol=1e-8, max_iter=100):
    for step in range(1, max_iter + 1):
        df_approx = func(r1) - func(r0)
        if abs(df_approx) < 1e-15:
            break
        r2 = r1 - func(r1) * (r1 - r0) / df_approx
        if abs(r2 - r1) < tol:
            return r2, step
        r0, r1 = r1, r2
    return r1, max_iter

rate_est, steps = secant_rate(balance_gap, 0.01, 0.08)
print("Estimated rate parameter:", round(rate_est, 6), "in", steps, "steps")
