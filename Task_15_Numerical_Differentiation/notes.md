# Task 15: Numerical Differentiation

Inputs and Mathematical Operations
- Smooth scalar function f(x) = sin(x) evaluated at x0 = 1.0 using forward difference and central difference formulas across step sizes h.
- Forward difference has first-order truncation error O(h), while central difference achieves second-order accuracy O(h^2).

Parameter Change
- Shrinking h improves truncation accuracy at first, but making h too small (such as 1e-12 or smaller) lets floating-point subtraction roundoff error grow and pollute the derivative estimate.

Output and Graph Interpretation
- Prints step size h alongside forward and central difference errors so you can observe central differences converging faster and see the roundoff trade-off.

Modified Real-World Case
- Assumptions: Position readings s(t) are sampled evenly every 0.5 seconds along a straight path.
- Inputs: Time array t from 0.0 to 3.0 seconds and corresponding position measurements s in meters.
- Output: Prints time, position, estimated velocity, and estimated acceleration at each sample point.
- Interpretation: Numerical differentiation turns discrete position logs into speed and acceleration profiles useful for motion analysis and control.
