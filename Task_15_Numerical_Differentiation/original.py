import numpy as np

def f(x):
    return np.sin(x)

def df_exact(x):
    return np.cos(x)

def forward_diff(func, x, h):
    return (func(x + h) - func(x)) / h

def central_diff(func, x, h):
    return (func(x + h) - func(x - h)) / (2.0 * h)

x0 = 1.0
exact = df_exact(x0)

for h in [1e-1, 1e-2, 1e-4, 1e-6, 1e-8]:
    fwd = forward_diff(f, x0, h)
    cen = central_diff(f, x0, h)
    err_fwd = abs(fwd - exact)
    err_cen = abs(cen - exact)
    print(f"h={h:8.1e} | fwd_err={err_fwd:10.2e} | cen_err={err_cen:10.2e}")
