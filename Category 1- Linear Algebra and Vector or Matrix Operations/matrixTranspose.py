import numpy as np


def transposeMatrix(matrix):
    """Transposes a NumPy matrix."""
    return matrix.T    # or np.transpose(matrix)


if __name__ == "__main__":
    # Test Cases
    matrix1 = np.array([[1, 2, 3],
                        [4, 5, 6]])  # 2x3

    print(f"Original matrix:\n{matrix1}")
    print(f"Transposed matrix:\n{transposeMatrix(matrix1)}")
    # Expected: [[1, 4], [2, 5], [3, 6]] (3x2)

    matrix2 = np.array([[1, 2],
                        [3, 4]])  # 2x2

    print(f"\nOriginal matrix:\n{matrix2}")
    print(f"Transposed matrix:\n{transposeMatrix(matrix2)}")



