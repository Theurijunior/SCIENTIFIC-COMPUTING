# Task 20: Monte Carlo Simulation

Inputs and Mathematical Operations
- Uniformly distributed random pairs (x, y) on the square [-1, 1] by [-1, 1] tested for whether x^2 + y^2 is less than or equal to 1 to estimate pi from area ratios.
- Monte Carlo sampling averages indicator outcomes across many random draws and measures statistical uncertainty via standard error.

Parameter Change
- Increasing sample count lowers standard error roughly in proportion to 1/sqrt(N), while changing the random seed produces a different draw sequence that still converges toward the same underlying expectation.

Output and Graph Interpretation
- Prints the sample size, estimated value of pi, absolute error against numpy.pi, and estimated standard error so you can gauge both accuracy and sampling spread.

Modified Real-World Case
- Assumptions: Daily network traffic demand and available link capacity vary independently across 30 days according to normal distributions, with an SLA breach flagged if overloaded days reach at least 3 in a month.
- Inputs: 50,000 simulated 30-day months with load mean 680 and std 75, and capacity mean 820 and std 55.
- Output: Prints average monthly overload days and estimated probability of 3 or more overload days in a month.
- Interpretation: Monte Carlo simulation evaluates risk probabilities in noisy multi-day systems where analytical formulas become messy or restrictive.
