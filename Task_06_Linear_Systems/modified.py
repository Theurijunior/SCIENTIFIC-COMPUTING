import numpy as np

# Real-world scenario: DC circuit node/mesh current analysis (Kirchhoff's laws)
# Resistance matrix R (in ohms) and source voltage vector V (in volts)
# Solve R * I = V for branch/mesh currents I (in amperes)

R = np.array([
    [10.0, -4.0, 0.0],
    [-4.0, 12.0, -3.0],
    [0.0, -3.0, 8.0]
])

V = np.array([24.0, 0.0, -12.0])

currents_A = np.linalg.solve(R, V)
voltage_check = R @ currents_A
residual = np.linalg.norm(voltage_check - V)

print("Resistance matrix R (ohms):\n", R)
print("\nVoltage vector V (volts):\n", V)
print("\nSolved mesh currents I (amperes):\n", np.round(currents_A, 6))
print(f"\nResidual norm ||R*I - V||_2: {residual:.2e}")
