import numpy as np


def cosine_similarity(vec_a, vec_b):
    """
        Calculates the cosine similarity between two NumPy vectors.
        Handles zero vectors gracefully.
    """
    if len(vec_a) != len(vec_b):
        return ValueError("Vectors must have the same dimension.")

    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)   # L2 norm
    norm_b = np.linalg.norm(vec_b)   # L2 norm

    if norm_a == 0 or norm_b == 0:
        # Edge case: handling zero vectors is important to avoid division by zero
        return 0.0

    return dot_product / (norm_a * norm_b)



if __name__ == "__main__":
    # Test Cases
    vec_doc1 = np.array([1, 1, 0, 1, 0, 1])
    vec_doc2 = np.array([1, 1, 1, 0, 1, 0])
    vec_doc3 = np.array([0, 0, 0, 0, 0, 0])

    print(f"Cosine similarity between doc1 and doc2: {cosine_similarity(vec_doc1, vec_doc2):.4f}")
    # Expected: (1*1 + 1*1 + 0*1 + 1*0 + 0*1 + 1*0) / (sqrt(4) * sqrt(4)) = 2 / (2 * 2) = 0.5

    vec_similar_a = np.array([1, 2, 3])
    vec_similar_b = np.array([2, 4, 6])  # Directly proportional, should be 1.0
    print(f"Cosine similarity between similar vectors: {cosine_similarity(vec_similar_a, vec_similar_b):.4f}")

    vec_orthogonal_a = np.array([1, 0])
    vec_orthogonal_b = np.array([0, 1])  # Orthogonal, should be 0.0
    print(f"Cosine similarity between orthogonal vectors: {cosine_similarity(vec_orthogonal_a, vec_orthogonal_b):.4f}")

    print(f"Cosine similarity with zero vector (doc1, doc3): {cosine_similarity(vec_doc1, vec_doc3):.4f}")