import numpy as np
from scipy.linalg import lu_factor, lu_solve

K = np.array([
    [15.0, -3.0, -2.0],
    [-3.0, 10.0, -4.0],
    [-2.0, -4.0, 12.0]
])

load_case_1 = np.array([100.0, 80.0, 60.0])
load_case_2 = np.array([140.0, 95.0, 50.0])

lu_and_piv = lu_factor(K)
disp_1 = lu_solve(lu_and_piv, load_case_1)
disp_2 = lu_solve(lu_and_piv, load_case_2)

print("Load case 1 response:", np.round(disp_1, 6))
print("Load case 2 response:", np.round(disp_2, 6))
