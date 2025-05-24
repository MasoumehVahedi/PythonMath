#### Category 1: Linear Algebra & Vector/Matrix Operations  
These are fundamental to almost all modern ML.

#### Question 1.1: Vector Norms (L1, L2, L-infinity)  
**Problem:** Given a 1D NumPy array (vector), write functions to calculate its L1 (Manhattan), L2 (Euclidean), and L-infinity (Max) norms.

**Mathematical Background**  
- **L1 Norm** \(\|\mathbf{x}\|_1\): Sum of the absolute values of the vector’s components.  
  \(\displaystyle \|\mathbf{x}\|_1 = \sum_{i=1}^{n} |x_i|\)

- **L2 Norm** \(\|\mathbf{x}\|_2\) (Euclidean norm): Square root of the sum of squared values of the vector’s components.  
  \(\displaystyle \|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}\)

- **L∞ Norm** \(\|\mathbf{x}\|_\infty\) (Max norm): The maximum absolute value among the vector’s components.  
  \(\displaystyle \|\mathbf{x}\|_\infty = \max_{i} |x_i|\)
