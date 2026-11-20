# Task 6: Linear Systems of Equations

## Input Values and Mathematical Operations
- **Input:** A $3 \times 3$ non-singular coefficient matrix $A$ and a right-hand side column/1D vector $b$.
- **Operations:** Solving the linear system $Ax = b$ via `np.linalg.solve(A, b)` and computing the Euclidean residual norm $\|Ax - b\|_2$ via `np.linalg.norm` to check solution accuracy.

## Parameter Change ("What-If")
- Changing an entry of $b$ scales or shifts the solution $x$ linearly because $x = A^{-1}b$, whereas making rows of $A$ proportional or linearly dependent produces a singular matrix where `np.linalg.solve` raises a `LinAlgError`.

## Meaning of Output
- Displays $A$, $b$, the computed solution vector $x = [x_1, x_2, x_3]$, and the residual norm $\|Ax - b\|_2$, confirming how closely substituting $x$ back into $Ax$ reproduces $b$.

## Modified Real-World Case: DC Mesh Circuit Current Analysis
- **Assumptions:** A three-mesh resistive DC network follows linear Ohm's and Kirchhoff's voltage laws, represented as $R \cdot I = V$ with symmetric mutual resistances on the off-diagonals and self-resistances on the diagonal.
- **Input Data:** $3 \times 3$ resistance matrix $R$ (in $\Omega$) and voltage source vector $V = [24.0, 0.0, -12.0]^T$ (in $\text{V}$).
- **Output:** Prints $R$, $V$, the solved mesh currents $I$ (in $\text{A}$), and the residual norm $\|RI - V\|_2$.
- **Interpretation:** Solving $RI = V$ yields steady-state loop currents across coupled resistive branches without manually substituting equations by hand.
