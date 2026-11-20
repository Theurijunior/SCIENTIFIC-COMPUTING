# Task 8: Iterative Linear Solvers (Jacobi and Gauss-Seidel)

Inputs and Mathematical Operations
- A strictly diagonally dominant 4 by 4 matrix A and right-hand side vector b solved iteratively using Jacobi and Gauss-Seidel updates until infinity-norm change falls below tolerance.
- Gauss-Seidel uses newly updated components immediately within the same sweep, whereas Jacobi updates from the previous iteration vector.

Parameter Change
- Tightening tolerance from 1e-8 to 1e-12 or starting from a nonzero initial guess changes iteration count, while weakening diagonal dominance slows convergence or can cause divergence.

Output and Graph Interpretation
- Shows the converged solution vectors, iteration counts for Jacobi and Gauss-Seidel, and a direct solve check so you can see how Gauss-Seidel typically converges in fewer steps.

Modified Real-World Case
- Assumptions: Four connected thermal nodes reach steady state starting from a 25 degree baseline with conductive coupling and fixed heat inputs.
- Inputs: Conductance matrix G and heat source vector [120.0, 80.0, 60.0, 40.0].
- Output: Prints the steady-state node temperatures and number of sweeps needed to converge.
- Interpretation: Iterative sweeps estimate coupled nodal temperatures cleanly without factoring large sparse matrices directly.
