# Task 9: Eigenvalues and Eigenvectors

Inputs and Mathematical Operations
- A symmetric 3 by 3 matrix A analyzed using NumPy eigenvalue decomposition and power iteration for the dominant eigenpair.
- Power iteration repeatedly multiplies a normalized vector by A and computes the Rayleigh quotient until convergence.

Parameter Change
- Changing off-diagonal coupling entries or swapping to a matrix with closely spaced top eigenvalues slows power iteration convergence, while scaling A by a constant multiplies eigenvalues by that same factor.

Output and Graph Interpretation
- Displays all eigenvalues, their corresponding eigenvectors, and the power-iteration estimate of the largest eigenvalue so you can verify the dominant mode.

Modified Real-World Case
- Assumptions: Telemetry observations across four correlated metrics are centered around their column means before forming a sample covariance matrix.
- Inputs: A 6 by 4 matrix of telemetry readings across four channels.
- Output: Prints sorted covariance eigenvalues, explained variance ratios, and the leading principal direction vector.
- Interpretation: Larger eigenvalues point to directions of stronger shared variation across channels, helping identify dominant patterns in multi-metric data.
