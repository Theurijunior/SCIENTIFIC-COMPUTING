# BIT 2118: Scientific Computing
DOCUMENTATION

Repository containing Python implementations and technical documentation for numerical methods and scientific computing coursework.

Author: Joe Kinyua
GitHub Repository: https://github.com/Theurijunior/SCIENTIFIC-COMPUTING

## Overview

This repository covers core numerical algorithms implemented in Python using NumPy and SciPy. Every task directory is organized into three files:

- original.py: Reference implementation demonstrating the standard numerical algorithm and behavior.
- modified.py: Adapted implementation applying the numerical method to a practical real-world scenario.
- notes.md: Technical documentation detailing inputs, mathematical operations, parameter sensitivity, output interpretation, and modeling assumptions.

## Environment and Requirements

- Python 3.10 or higher
- NumPy
- SciPy

Install the required packages:

```bash
pip install numpy scipy
```

## Running the Code

Navigate to any task directory and execute either script:

```bash
cd task_02
python original.py
python modified.py
```

## Repository Contents

- task_02: Array Creation, Indexing, and Vectorization
- task_03: Floating-Point Arithmetic and Numerical Errors
- task_04: Matrix Algebra and Decomposition
- task_05: Direct Linear Solvers (Gaussian Elimination and LU)
- task_06: Matrix Conditioning and Stability
- task_07: Least-Squares Linear Systems and QR Decomposition
- task_08: Iterative Linear Solvers (Jacobi and Gauss-Seidel)
- task_09: Eigenvalues and Eigenvectors
- task_10: Bisection and Fixed-Point Iteration
- task_11: Newton and Secant Methods
- task_12: Systems of Nonlinear Equations
- task_13: Interpolation (Linear and Cubic Spline)
- task_14: Curve Fitting and Least Squares
- task_15: Numerical Differentiation
- task_16: Numerical Integration (Trapezoidal and Simpson Rules)
- task_17: Ordinary Differential Equations (Euler Method)
- task_18: Runge-Kutta Methods (RK4 and RK45)
- task_19: Numerical Optimization (BFGS and Gradient Descent)
- task_20: Monte Carlo Simulation

## Documentation

Full task-level documentation is included inside each task folder under notes.md, outlining:
1. Inputs and Mathematical Operations
2. Parameter Change Effects
3. Output and Graph Interpretation
4. Modified Real-World Case (Assumptions, Inputs, Output, and Interpretation)
