import numpy as np

# Real-world scenario: evaluating 2D spatial transformation / scaling-rotation
# matrices on a set of 2D coordinate points (e.g., node positions on a grid/map)

# 2D transformation matrix (scaling + shear/rotation)
T = np.array([
    [1.2, 0.2],
    [-0.15, 1.1]
])

# Rows are 2D points (x, y)
points = np.array([
    [10.0, 20.0],
    [15.0, 25.0],
    [12.0, 30.0],
    [18.0, 22.0]
])

# Apply transformation to all points at once: (N x 2) @ (2 x 2).T -> (N x 2)
transformed_points = points @ T.T
det_T = np.linalg.det(T)
inv_T = np.linalg.inv(T)
recovered_points = transformed_points @ inv_T.T

print("Transformation matrix T:\n", T)
print(f"\nDeterminant of T (area scale factor): {det_T:.4f}")
print("\nTransformed coordinates:\n", np.round(transformed_points, 3))
print("\nRecovered original coordinates via T^-1:\n", np.round(recovered_points, 6))
