# Task 18: Runge-Kutta Methods (RK4 and RK45)

Inputs and Mathematical Operations
- Initial value problem dy/dt = -0.5y + sin(2t) with y(0) = 2 over [0.0, 6.0] solved via a classical fourth-order Runge-Kutta loop and compared against SciPy solve_ivp using RK45.
- RK4 evaluates four intermediate slopes per step to reach fourth-order local/global accuracy without needing higher derivatives.

Parameter Change
- Adjusting transmission rate beta or recovery rate gamma in the coupled model shifts peak infection timing and severity, while tighter tolerances in solve_ivp refine adaptive step sizes.

Output and Graph Interpretation
- Prints final state values from both RK4 and RK45 along with the maximum difference across evaluation points so you can verify close agreement.

Modified Real-World Case
- Assumptions: Total population is normalized to 1 across susceptible, infectious, and recovered compartments with constant transmission and recovery rates over 30 days.
- Inputs: Initial state [0.99, 0.01, 0.0], beta = 0.35, and gamma = 0.10 evaluated every 5 days up to day 30.
- Output: Prints susceptible, infectious, and recovered fractions at sampled days across the 30-day period.
- Interpretation: Runge-Kutta integration models nonlinear coupled compartment dynamics cleanly as susceptible individuals move into infectious and recovered states.
