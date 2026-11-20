# Task 19: Numerical Optimization (BFGS and Gradient Descent)

Inputs and Mathematical Operations
- Multivariable scalar function (x - 2)^2 + 3*(y + 1.5)^2 + sin(x) minimized using BFGS with an analytical gradient and compared against fixed-step gradient descent.
- Optimization searches for points where the gradient approaches zero and objective value reaches a local minimum.

Parameter Change
- Changing learning rate in gradient descent can slow progress if too small or overshoot and diverge if too large, while adding bounds restricts the search space to feasible values.

Output and Graph Interpretation
- Prints the minimizer coordinates and lowest objective value so you can check convergence and compare quasi-Newton BFGS against plain gradient descent.

Modified Real-World Case
- Assumptions: Demand occurs steadily over the year with fixed per-order setup cost and linear holding cost proportional to average stock level.
- Inputs: Annual demand of 12000 units, order cost of 45, and holding cost of 2.4 with positive batch size bound.
- Output: Prints the optimal order batch size and minimum annual total cost.
- Interpretation: Numerical optimization balances competing trade-offs like ordering frequency against storage cost to find an operating sweet spot.
