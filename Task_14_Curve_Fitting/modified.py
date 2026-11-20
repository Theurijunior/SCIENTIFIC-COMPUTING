import numpy as np
from scipy.optimize import curve_fit

# Real-world case: modeling service response time (ms) as a function of concurrent load
# Model: latency(load) = base_ms + scale_ms * exp(rate * load)

load_users = np.array([10.0, 25.0, 40.0, 55.0, 70.0, 85.0, 100.0])
latency_ms = np.array([18.5, 21.0, 25.4, 32.8, 44.5, 63.0, 91.2])

def latency_model(load, base_ms, scale_ms, rate):
    return base_ms + scale_ms * np.exp(rate * load)

popt, _ = curve_fit(
    latency_model,
    load_users,
    latency_ms,
    p0=[15.0, 2.0, 0.03],
    maxfev=10000
)

base_est, scale_est, rate_est = popt
pred_ms = latency_model(load_users, base_est, scale_est, rate_est)
rmse = np.sqrt(np.mean((latency_ms - pred_ms) ** 2))

print(f"Fitted base: {base_est:.2f} ms, scale: {scale_est:.4f}, rate: {rate_est:.4f}")
print(f"Fit RMSE: {rmse:.3f} ms")
print(f"Predicted latency at 120 users: {latency_model(120.0, *popt):.2f} ms")
