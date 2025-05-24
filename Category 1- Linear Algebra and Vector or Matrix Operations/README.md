#### Category 1: Linear Algebra & Vector/Matrix Operations  
These are fundamental to almost all modern ML.

#### Question 1.1: Vector Norms (L1, L2, L-infinity)  
**Problem:** Given a 1D NumPy array (vector), write functions to calculate its L1 (Manhattan), L2 (Euclidean), and L-infinity (Max) norms.

**Mathematical Background**  
- **L1 Norm** ($$\|x\|_1$$): Sum of the absolute values of the vector's components, $$ \|x\|_1 = \sum_{i=1}^{n} |x_i| $$.

- **L2 Norm** ($$\|x\|_2$$): Square root of the sum of the squared values of the vector's components, $$ \|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2} $$.

- **L-infinity Norm** ($$\|x\|_\infty$$): The maximum absolute value among the vector's components, $$ \|x\|_\infty = \max_i |x_i| $$.

#### Question 1.2: Vector Normalization (Unit Vector)

**Problem:** Given a 1D NumPy array (`vector`), write a function to normalize it to a unit vector (i.e., its L₂ norm becomes 1). Handle the case of a zero vector.

**Mathematical Background:**  
To normalize a vector **x** to a unit vector **x̂**, you divide each component by its L₂ norm:  
$$\hat{x} \;=\;\frac{x}{\|x\|_{2}}$$
