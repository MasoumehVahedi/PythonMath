"""
    PROBLEM:
    A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach
    the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
    How many possible unique paths are there?

    Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
    Example :

    Input : A = 2, B = 2
    Output : 2

    2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
                  OR  : (0, 0) -> (1, 0) -> (1, 1)


    SOLUTION:
    This is a classic combinatorics problem disguised as a path-finding problem. Let me break it down:

    Grid Setup: We have an A×B grid (A rows, B columns)
    Movement Rules: Robot can only move RIGHT or DOWN
    Goal: Count unique paths from top-left (0,0) to bottom-right (A-1, B-1)

    Key Insight
    To reach the bottom-right corner, the robot must make:

    (A-1) down moves (to go from row 0 to row A-1)
    (B-1) right moves (to go from column 0 to column B-1)

    Total moves needed: (A-1) + (B-1) = A + B - 2

    The Mathematical Solution (without repetition):
    This becomes a combinations problem: "In how many ways can we arrange (A-1) down moves and (B-1) right moves?"
    The answer is: C(A+B-2, A-1) or equivalently C(A+B-2, B-1)
    Where C(n,k) = n! / (k! × (n-k)!)
"""

import math


def uniquePaths(A, B):
    """
       combinations formula: C(n,k) = n!/k!(n-k)!
           - n is the total number of items in the set.
           - k is the number of items to be selected from the set.
           - n! represents the factorial of n, i.e. the product of all positive integers up to n.
    """
    n = A + B - 2
    k = A - 1
    return math.comb(n, k)


def visualizePaths(A, B):
    """
    Helper function to visualize the grid and show path counts for small grids.
    """
    if A > 5 or B > 5:
        print("Grid too large to visualize")
        return

    print(f"\nPath counts for {A}x{B} grid:")
    print("=" * 30)

    # Calculate paths to each cell
    dp = [[0] * B for _ in range(A)]

    for j in range(B):
        dp[0][j] = 1
    for i in range(A):
        dp[i][0] = 1


    for i in range(1, A):
        for j in range(1, B):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


    for i in range(A):
        for j in range(B):
            print(f"{dp[i][j]:3}", end=" ")
        print()

    print(f"\nTotal unique paths: {dp[A - 1][B - 1]}")




if __name__ == "__main__":
    test_cases = [
        (2, 2, 2),
        (3, 3, 6),  # 3x3 grid
        (3, 2, 3),  # 3x2 grid
        (1, 1, 1),  # Edge case: 1x1 grid
        (4, 4, 20),
    ]

    print("Testing all solutions:")
    print("=" * 50)

    for A, B, expected in test_cases:
        print(f"\nGrid: {A}x{B} (Expected: {expected})")

        result1 = uniquePaths(A, B)
        print(f"Combinatorial: {result1}")

    # Visualize small examples
    visualizePaths(2, 2)
    visualizePaths(3, 3)

    # Performance comparison for larger input
    print(f"\nFor 10x10 grid: {uniquePaths(10, 10)} paths")
