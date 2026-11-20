import numpy as np

# Real-world case: principal modes / covariance analysis of 4 network latency
# and packet-loss telemetry channels across 6 observation windows
telemetry = np.array([
    [18.0, 12.0, 22.0, 15.0],
    [20.0, 14.0, 24.0, 16.0],
    [16.0, 11.0, 19.0, 13.0],
    [25.0, 18.0, 28.0, 20.0],
    [14.0, 10.0, 17.0, 12.0],
    [22.0, 15.0, 26.0, 18.0]
])

centered = telemetry - np.mean(telemetry, axis=0)
cov_matrix = np.cov(centered, rowvar=False)
evals, evecs = np.linalg.eigh(cov_matrix)

# Sort from largest to smallest eigenvalue
idx = np.argsort(evals)[::-1]
evals = evals[idx]
evecs = evecs[:, idx]

variance_ratio = evals / np.sum(evals)
print("Covariance eigenvalues:", np.round(evals, 4))
print("Explained variance ratios:", np.round(variance_ratio, 4))
print("Top principal component:", np.round(evecs[:, 0], 4))
