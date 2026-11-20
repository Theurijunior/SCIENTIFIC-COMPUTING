import math

# Real-world case: finding break-even unit price or demand threshold
# where net revenue minus fixed cost equals zero: P(q)*q - FC = 0
# Using scaled equation f(q) = 0.02*q^2 + 15*q - 1800 = 0 for q > 0

def net_balance(q):
    return 0.02 * q**2 + 15.0 * q - 1800.0

def bisection_threshold(func, low, high, tol=1e-6, max_iter=100):
    for step in range(1, max_iter + 1):
        mid = 0.5 * (low + high)
        if abs(func(mid)) < tol or (high - low) < tol:
            return mid, step
        if func(low) * func(mid) < 0:
            high = mid
        else:
            low = mid
    return 0.5 * (low + high), max_iter

q_root, steps = bisection_threshold(net_balance, 0.0, 200.0)
print("Break-even volume:", round(q_root, 4), "units in", steps, "steps")
