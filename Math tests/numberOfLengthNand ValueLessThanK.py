"""
    Given a set of digits (A) in sorted order, find how many numbers can be formed using these digits
    such that its length is B and whose value is less than the number C.
    NOTE: All numbers can only have digits from the given set.

    Problem Constraints
        0 <= |A| <= 10
        1 <= B <= 9
        0 <= C <= 1e9
        0 <= A[i] <= 9


    Input Format
        The first argument is an integer array A.
        The second argument is an integer B.
        The third argument is an integer C.


    Output Format
        Return an integer.


    Example Input
        Input 1:
        A = [0, 1, 5]
        B = 1
        C = 2
        Input 2:
        A = [0, 1, 2, 5]
        B = 2
        C = 21

"""

MAX = 10

def numToVec(N):
    """ Function to convert a number into vector """
    digit = []

    # Push all the digits of N from the end
    while N != 0:
        digit.append(N % 10)
        N = N // 10

    if len(digit) == 0:
        digit.append(0)

    # Reverse the vector elements
    digit = digit[::-1]

    return digit


def solution(A, B, C):
    """ Function to return the count of B length integers
        which are less than C and they contain digits from set A[] only.
    """
    digit = numToVec(C)
    length = len(A)    # total number of available digits

    # Case 1: Impossible cases, greater than C
    if B > len(digit) or length == 0:
        return 0

    # Case 2: All integers of length B are valid as they all are less than C
    elif B < len(digit):
        # If 0 is available and B > 1, we can't start with 0. Example: 00, 01, 02, ← INVALID (start with 0)
        if 0 in A and B != 1:
            # (d - 1) = choices for first position (can't use 0)
            # length ** (B - 1) = choices for remaining positions (can use any digit)
            return (length - 1) * (length ** (B - 1))
        else:
            # Example: A = [0, 1, 2], B = 2 ----> length^B = 3^2 = 9 combinations
            return length ** B

    # Case 3: B == length of C (need dynamic programming)
    else:
        dp = [0] * (B + 1)    # or [0 for i in range(B + 1)]
        lower = [0] * (MAX + 1)

        # Create lookup table: lower[i] = count of digits in A that are < i
        for digit_val in A:
            lower[digit_val + 1] = 1
        # Convert to cumulative sum
        for i in range(1, MAX + 1):
            lower[i] = lower[i - 1] + lower[i]

        flag = True  # Whether we're still bounded by C's digits
        dp[0] = 0

        for i in range(1, B + 1):
            d = lower[digit[i - 1]]   # Count of available digits < current digit of C
            dp[i] = dp[i-1] * length

            # For first position, can't use 0 if B > 1
            if i == 1 and 0 in A and B != 1:
                d = d - 1

            # If still bounded by C, add choices for current position
            if flag:
                dp[i] += d

            # Check if current digit of C is available in A
            # If not, we're no longer bounded by C for subsequent positions
            flag = flag and (lower[digit[i-1] + 1] == lower[digit[i-1]] + 1)

    return dp[B]


if __name__ == "__main__":
    # Test Case 1
    A1 = [0, 1, 5]
    B1 = 1
    C1 = 2
    result1 = solution(A1, B1, C1)
    print(f"Test 1: A={A1}, B={B1}, C={C1} -> Result: {result1}")

    # Test Case 2
    A2 = [0, 1, 2, 5]
    B2 = 2
    C2 = 21
    result2 = solution(A2, B2, C2)
    print(f"Test 2: A={A2}, B={B2}, C={C2} -> Result: {result2}")












