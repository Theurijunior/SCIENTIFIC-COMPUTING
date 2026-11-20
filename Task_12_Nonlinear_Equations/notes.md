# Task 12: Systems of Nonlinear Equations

Inputs and Mathematical Operations
- A coupled system of two nonlinear equations in two unknowns (x and y) solved numerically using SciPy root finders with an analytical Jacobian matrix provided.
- Multidimensional root finding drives both residual equations to zero simultaneously rather than solving one variable at a time.

Parameter Change
- Shifting the initial guess into a different quadrant or region can lead to a different valid intersection point (for instance, a circle and a line intersect at two points), while a poor guess far from any solution can slow or fail convergence.

Output and Graph Interpretation
- Prints the solved (x, y) coordinates from fsolve and root along with the residual norm so you can verify how close the equations are to zero at the solution.

Modified Real-World Case
- Assumptions: Two coupled system parameters x and y must simultaneously satisfy two nonlinear balance equations near a positive operating point.
- Inputs: Coupled equations 0.4*x^2 + 1.5*y - 40 = 0 and 2.0*x - 0.8*y^2 + 3 = 0 with initial guess [6.0, 5.0].
- Output: Prints the solved (x, y) operating point, convergence status, and residual values.
- Interpretation: Solving coupled nonlinear equations finds joint equilibrium values where multiple interacting constraints hold together.
