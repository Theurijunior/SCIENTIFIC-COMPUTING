# Task 13: Interpolation (Linear and Cubic Spline)

Inputs and Mathematical Operations
- Known data pairs (x_known, y_known) interpolated at intermediate query points x_eval using piecewise linear interpolation and natural cubic spline interpolation.
- Piecewise linear connects adjacent points with straight segments, while cubic splines fit piecewise cubic polynomials with continuous first and second derivatives across interior knots.

Parameter Change
- Changing boundary conditions (such as natural vs. clamped spline slopes) or adding more sample points near sharp turns changes curve smoothness and intermediate estimates between known points.

Output and Graph Interpretation
- Displays evaluated positions and interpolated values for both linear and cubic spline methods so you can see how smooth curves round corners compared to sharp straight-line segments.

Modified Real-World Case
- Assumptions: Trail elevation varies smoothly between checkpoint measurements along a 10 km route.
- Inputs: Checkpoint distances in kilometers and elevations in meters sampled at five intermediate distances.
- Output: Prints the estimated elevation in meters at each intermediate distance along the route.
- Interpretation: Cubic spline interpolation estimates missing elevations between checkpoints smoothly, helping map terrain profiles without extra field readings.
