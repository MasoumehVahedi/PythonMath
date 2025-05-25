import numpy as np


def matrixMultiply(matrix_a, matrix_b):
    """
        Performs matrix multiplication of two NumPy matrices.
    """
    return np.dot(matrix_a, matrix_b)



if __name__ == "__main__":
    # Test Cases
    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    C_expected = np.array([[1 * 5 + 2 * 7, 1 * 6 + 2 * 8],
                           [3 * 5 + 4 * 7, 3 * 6 + 4 * 8]])
    # C_expected = [[19, 22], [43, 50]]

    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    print(f"Matrix A x B:\n{matrixMultiply(A, B)}")
    print(f"Expected:\n{C_expected}")

    D = np.array([[1, 2, 3],
                  [4, 5, 6]])  # 2x3 matrix

    E = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])  # 3x2 matrix

    print(f"\nMatrix D:\n{D}")
    print(f"Matrix E:\n{E}")
    print(f"Matrix D x E:\n{matrixMultiply(D, E)}")