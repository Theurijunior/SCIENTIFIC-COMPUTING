import numpy as np
from scipy.interpolate import interp1d, CubicSpline

x_known = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y_known = np.array([1.0, 2.5, 2.0, 4.5, 6.0, 5.5])

x_eval = np.array([0.5, 1.5, 2.5, 3.5, 4.5])

linear_interp = interp1d(x_known, y_known, kind="linear")
spline_interp = CubicSpline(x_known, y_known, bc_type="natural")

y_linear = linear_interp(x_eval)
y_spline = spline_interp(x_eval)

print("Evaluation points x:", x_eval)
print("Linear interpolation y:", np.round(y_linear, 4))
print("Cubic spline y:", np.round(y_spline, 4))
