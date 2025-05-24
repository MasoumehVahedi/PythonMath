import numpy as np


def normalizeVector(vector):
    """
        Normalizes a NumPy vector to a unit vector (L2 norm = 1).
        Handles zero vectors to prevent division by zero.
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return np.zeros_like(vector)  # Return a zero vector of same shape
    return vector / norm



if __name__ == "__main__":
    # Test Cases
    vec1 = np.array([3, 4])
    normalized_vec1 = normalizeVector(vec1)
    print(f"Original vector: {vec1}")
    print(f"Normalized vector: {normalized_vec1}")
    print(f"L2 norm of normalized vector: {np.linalg.norm(normalized_vec1):.2f}")

    vec2 = np.array([1, 1, 1])
    normalized_vec2 = normalizeVector(vec2)
    print(f"\nOriginal vector: {vec2}")
    print(f"Normalized vector: {normalized_vec2}")
    print(f"L2 norm of normalized vector: {np.linalg.norm(normalized_vec2):.2f}")

    vec3 = np.array([0, 0, 0])
    normalized_vec3 = normalizeVector(vec3)
    print(f"\nOriginal vector: {vec3}")
    print(f"Normalized vector (zero vector): {normalized_vec3}")
    print(f"L2 norm of normalized vector: {np.linalg.norm(normalized_vec3):.2f}")
