# Task 10: Bisection and Fixed-Point Iteration

Inputs and Mathematical Operations
- Nonlinear scalar equation f(x) = x^3 - x - 2 solved on bracket [1.0, 2.0] via bisection, and reformulated as x = g(x) = (x + 2)^(1/3) starting at x0 = 1.5 for fixed-point iteration.
- Bisection halves the bracket each step based on sign changes, while fixed-point iteration repeatedly applies g(x).

Parameter Change
- Widening the bracket or tightening tolerance from 1e-8 to 1e-12 increases bisection steps predictably, while picking a g(x) with |g'(x)| greater than or equal to 1 near the root can make fixed-point iteration diverge.

Output and Graph Interpretation
- Prints the estimated root and iteration count for both methods so you can compare guaranteed bracket contraction against fixed-point convergence.

Modified Real-World Case
- Assumptions: A positive operating threshold q lies between 0 and 200 units where net_balance(q) crosses zero.
- Inputs: Quadratic balance model 0.02*q^2 + 15*q - 1800 over bracket [0.0, 200.0].
- Output: Prints the break-even unit count and number of bisection steps taken.
- Interpretation: Bracketed root finding reliably locates a threshold whenever the sign flips across the search interval.
