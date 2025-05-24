#### Category 1: Linear Algebra & Vector/Matrix Operations  
These are fundamental knowledge to almost all modern ML.

#### Question 1.1: Vector Norms (L1, L2, L-infinity)  
**Problem:** Given a 1D NumPy array (vector), write functions to calculate its L1 (Manhattan), L2 (Euclidean), and L-infinity (Max) norms.

**Mathematical Background:**  
- **L1 Norm** (‖x‖₁): Sum of the absolute values of the vector’s components.  
  \[
    \lVert x \rVert_{1} = \sum_{i=1}^{n} \lvert x_i \rvert
  \]
- **L2 Norm** (‖x‖₂): Square root of the sum of the squared values of the vector’s components, also known as the Euclidean norm.  
  \[
    \lVert x \rVert_{2} = \sqrt{\sum_{i=1}^{n} x_i^2}
  \]
- **L-infinity Norm** (‖x‖₍∞₎): The maximum absolute value among the vector’s components.  
  \[
    \lVert x \rVert_{\infty} = \max_{i} \lvert x_i \rvert
  \]
