import numpy as np


def l1_norm(vector):
    """Calculates the L1 norm of a NumPy vector."""
    return np.sum(np.abs(vector))


def l2_norm(vector):
    """Calculates the L2 norm (Euclidean) of a NumPy vector."""
    return np.sqrt(np.sum(vector**2))


def l_infinity_norm(vector):
    """Calculates the L-infinity norm of a NumPy vector."""
    return np.max(np.abs(vector))



if __name__ == "__main__":
    # Test Cases
    vec1 = np.array([3, -4])
    print(f"Vector: {vec1}")
    print(f"L1 Norm: {l1_norm(vec1)}")
    print(f"L2 Norm: {l2_norm(vec1)}")
    print(f"L-infinity Norm: {l_infinity_norm(vec1)}")

    vec2 = np.array([1, 2, 3])
    print(f"\nVector: {vec2}")
    print(f"L1 Norm: {l1_norm(vec2)}")  
    print(f"L2 Norm: {l2_norm(vec2)}")
    print(f"L-infinity Norm: {l_infinity_norm(vec2)}")

    vec3 = np.array([0, 0, 0])
    print(f"\nVector: {vec3}")
    print(f"L1 Norm: {l1_norm(vec3)}")
    print(f"L2 Norm: {l2_norm(vec3)}")
    print(f"L-infinity Norm: {l_infinity_norm(vec3)}")
