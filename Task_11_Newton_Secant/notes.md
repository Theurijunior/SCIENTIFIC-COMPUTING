# Task 11: Newton and Secant Methods

Inputs and Mathematical Operations
- Nonlinear equation f(x) = x^3 - 4x - 9 solved using Newton's method (requiring analytical derivative df/dx) and the secant method (approximating slope from two recent points).
- Both methods update root estimates iteratively until consecutive step changes drop below tolerance.

Parameter Change
- Starting far from the root or near a flat slope where the derivative is small can slow convergence or send iterates wide, while secant avoids writing an analytical derivative at the cost of slightly more steps than Newton.

Output and Graph Interpretation
- Prints the root estimate and iteration count for both Newton's method and the secant method so you can compare fast tangent convergence against derivative-free secant steps.

Modified Real-World Case
- Assumptions: A target balance gap depends smoothly on a rate parameter r near the 0.01 to 0.08 range without needing an explicit derivative formula.
- Inputs: Polynomial balance equation 1200 * (1 + 6*r + 15*r^2) - 1500 with initial guesses r0 = 0.01 and r1 = 0.08.
- Output: Prints the estimated rate parameter and number of secant iterations taken.
- Interpretation: The secant method locates parameter values quickly when computing or differentiating the exact slope is inconvenient.
