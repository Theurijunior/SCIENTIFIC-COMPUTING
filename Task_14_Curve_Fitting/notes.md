# Task 14: Curve Fitting and Least Squares

Inputs and Mathematical Operations
- Noisy paired observations (x_data, y_data) fitted using polynomial least squares via np.polyfit and nonlinear least squares via scipy.optimize.curve_fit.
- Least squares minimizes the sum of squared residuals between observed data and model predictions.

Parameter Change
- Increasing polynomial degree or changing the model structure alters bias and variance: an overly flexible curve can overfit noise, while a model whose shape mismatches the trend leaves higher residuals.

Output and Graph Interpretation
- Prints the fitted parameters and root mean square error (RMSE) for each model so you can compare how closely each curve tracks the observed points.

Modified Real-World Case
- Assumptions: Observed response latency rises nonlinearly as concurrent load increases, approximated by a baseline plus exponential growth term.
- Inputs: Seven load levels from 10 to 100 users paired with measured latency values in milliseconds.
- Output: Prints estimated model parameters, fit RMSE, and projected latency at 120 users.
- Interpretation: Fitting a parametric trend to noisy measurements helps summarize system behavior and project performance at higher loads with caution.
