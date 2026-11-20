# Task 16: Numerical Integration (Trapezoidal and Simpson Rules)

Inputs and Mathematical Operations
- Function f(x) = exp(-x^2) integrated over [0.0, 2.0] using composite trapezoidal and Simpson rules across subinterval counts n, compared against adaptive quadrature.
- Trapezoidal approximates each strip with a straight line segment, while Simpson fits parabolic arcs across pairs of subintervals for higher-order accuracy.

Parameter Change
- Increasing subintervals n reduces discretization error for both methods, with Simpson rule shrinking error much faster as n grows because its error scales with 1/n^4 instead of 1/n^2.

Output and Graph Interpretation
- Prints subinterval count n along with absolute errors for trapezoidal and Simpson integration relative to adaptive quadrature so you can compare convergence rates.

Modified Real-World Case
- Assumptions: Instantaneous power load changes smoothly between hourly meter readings across a 24-hour period.
- Inputs: Hourly time stamps from 0 to 24 hours and corresponding power readings in kilowatts.
- Output: Prints total energy consumed in kilowatt-hours and average power draw in kilowatts over the 24-hour span.
- Interpretation: Integrating power over time converts load profiles into total energy usage for billing, capacity planning, and load balancing.
