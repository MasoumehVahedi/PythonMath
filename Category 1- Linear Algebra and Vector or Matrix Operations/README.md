#### Category 1: Linear Algebra & Vector/Matrix Operations  
These are fundamental to almost all modern ML.

#### Question 1.1: Vector Norms (L1, L2, L-infinity)  
**Problem:** Given a 1D NumPy array (vector), write functions to calculate its L1 (Manhattan), L2 (Euclidean), and L-infinity (Max) norms.

**Mathematical Background**  
- **L1 Norm** ($$\|x\|_1$$): Sum of the absolute values of the vector's components, $$\|x\|_1 = \sum_{i=1}^{n} |x_i|$$.

- **L2 Norm** ($$\|x\|_2$$): Square root of the sum of the squared values of the vector's components, $$\|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}$$.

- **L-infinity Norm** ($$\|x\|_\infty$$): The maximum absolute value among the vector's components, $$\|x\|_\infty = \max_i |x_i|$$.

#### Question 1.2: Vector Normalization (Unit Vector)

**Problem:** Given a 1D NumPy array (`vector`), write a function to normalize it to a unit vector (i.e., its L₂ norm becomes 1). Handle the case of a zero vector.

**Mathematical Background:**  
To normalize a vector **x** to a unit vector **x̂**, you divide each component by its L₂ norm:  
$$\hat{x}=\frac{x}{\|x\|_{2}}$$

#### Question 1.3: Cosine Similarity

**Problem:** Given two 1D NumPy arrays (vectors) representing word embeddings or document vectors, calculate their cosine similarity.

**Mathematical Background:** Cosine similarity measures the cosine of the angle between two non-zero vectors. It is a measure of similarity between two vectors of an inner product space.
The formula for cosine similarity is:

$$\mathop{\text{cosine_similarity}}(A, B) = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

#### Question 1.4: Matrix Multiplication

**Problem:** Given two 2D NumPy arrays (matrices), write a function to perform their matrix multiplication.

**Mathematical Background:**
If matrix $A$ is $m \times n$ and matrix $B$ is $n \times p$, their product $C$ is an $m \times p$ matrix where:

$$C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$$

The number of columns in the first matrix must equal the number of rows in the second matrix.




