import numpy as np
from scipy.optimize import curve_fit

x_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
y_data = np.array([2.4, 4.1, 6.3, 8.2, 9.9, 12.1, 13.8, 16.2])

# Linear least-squares fit: y = m * x + c
m_poly, c_poly = np.polyfit(x_data, y_data, deg=1)

# Nonlinear curve fit using curve_fit: y = a * x + b * sin(x)
def model_func(x, a, b):
    return a * x + b * np.sin(x)

params, _ = curve_fit(model_func, x_data, y_data, p0=[2.0, 0.5])
a_fit, b_fit = params

y_pred_poly = m_poly * x_data + c_poly
y_pred_curve = model_func(x_data, a_fit, b_fit)

rmse_poly = np.sqrt(np.mean((y_data - y_pred_poly) ** 2))
rmse_curve = np.sqrt(np.mean((y_data - y_pred_curve) ** 2))

print(f"Linear fit: y = {m_poly:.4f} * x + {c_poly:.4f} (RMSE: {rmse_poly:.4f})")
print(f"Curve fit:  y = {a_fit:.4f} * x + {b_fit:.4f} * sin(x) (RMSE: {rmse_curve:.4f})")
