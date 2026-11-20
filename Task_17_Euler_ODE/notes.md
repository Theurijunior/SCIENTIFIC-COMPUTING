# Task 17: Ordinary Differential Equations (Euler Method)

Inputs and Mathematical Operations
- First-order initial value problem dy/dt = -2y + 1 with y(0) = 0 over [0.0, 2.0] solved using explicit Euler stepping across varying step counts.
- Each step advances the solution using the slope evaluated at the current time and state multiplied by step size h.

Parameter Change
- Using more steps reduces step size h and improves first-order accuracy O(h), while a step size too large relative to the decay rate can cause oscillation or numerical instability.

Output and Graph Interpretation
- Prints step count n, simulated value at t = 2.0, and absolute error against the closed-form solution so you can see accuracy improve as h shrinks.

Modified Real-World Case
- Assumptions: Heat loss follows Newton's law of cooling with constant cooling rate k = 0.15 per minute and a steady 24 degree ambient room temperature.
- Inputs: Initial temperature of 78 degrees, cooling rate 0.15, ambient temperature 24 degrees, and 60 steps across 30 minutes.
- Output: Prints temperature readings in Celsius at selected time points from start to 30 minutes.
- Interpretation: Euler stepping tracks how a warm component cools toward ambient temperature over time when an analytical formula is replaced or checked numerically.
