# Task 7: Gaussian Elimination and LU Decomposition

Inputs and Mathematical Operations
- A 3 by 3 coefficient matrix A and right-hand side vector b solved via manual Gaussian elimination with partial pivoting and compared against SciPy LU decomposition.
- Partial pivoting swaps rows so the largest pivot sits on the diagonal, reducing division by small numbers.

Parameter Change
- Changing an entry in b resolves the system directly without redoing row reduction when LU factors are already computed, while changing a row in A alters the pivot choices and factors.

Output and Graph Interpretation
- Prints the solution vector from both Gaussian elimination and LU solving along with matrices L and U so you can verify they match and check triangular structure.

Modified Real-World Case
- Assumptions: A system with matrix K is tested under two different right-hand load vectors using one precomputed LU factorization.
- Inputs: Matrix K and two load vectors, [100.0, 80.0, 60.0] and [140.0, 95.0, 50.0].
- Output: Prints the resulting response vectors for both load cases.
- Interpretation: Reusing an LU factorization saves repeated elimination work when solving the same system across multiple operating or load conditions.

