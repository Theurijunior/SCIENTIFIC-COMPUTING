# Task 5: Matrix Algebra

## Input Values and Mathematical Operations
- **Input:** Two $3 \times 3$ numeric matrices, $A$ and $B$, defined as NumPy `float64` arrays.
- **Operations:** Matrix transposition ($A^T$), matrix multiplication ($AB$ and $BA$ via `@`), determinant computation ($\det(A)$ via `np.linalg.det`), matrix inversion ($A^{-1}$ via `np.linalg.inv`), and identity verification ($A A^{-1} \approx I$).

## Parameter Change ("What-If")
- Modifying a row or column of $A$ so the rows become linearly dependent drives $\det(A) \to 0$, making $A$ singular (non-invertible) and causing `np.linalg.inv` to raise a `LinAlgError`.

## Meaning of Output
- Shows $A^T$, compares $AB$ against $BA$ to demonstrate that matrix multiplication is generally non-commutative, reports $\det(A)$, prints $A^{-1}$, and confirms $A A^{-1}$ equals the identity matrix up to floating-point rounding.

## Modified Real-World Case: 2D Coordinate Transformation and Inverse Recovery
- **Assumptions:** A $2 \times 2$ linear transformation matrix $T$ maps 2D spatial coordinates $(x, y)$ into a transformed coordinate frame, and its inverse $T^{-1}$ maps transformed coordinates back to the original frame.
- **Input Data:** A $2 \times 2$ matrix $T$ and four 2D coordinate pairs stored in a $4 \times 2$ array.
- **Output:** Displays $T$, the determinant of $T$ (area scaling factor), the transformed coordinates, and the recovered original coordinates after applying $T^{-1}$.
- **Interpretation:** Matrix multiplication applies linear coordinate mappings across all points cleanly in one operation, while $\det(T) \neq 0$ guarantees the transformation is invertible without losing spatial dimensions.
