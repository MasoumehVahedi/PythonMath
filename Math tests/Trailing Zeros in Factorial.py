"""
    Trailing Zeros in Factorial

    Question:
        Given an integer n, return the number of trailing zeros in n! (n factorial).
        Your solution should run in O(log n) time complexity.

    Solution Overview:
        Each trailing zero in n! comes from a factor pair (2 × 5).
        Since there are always more 2s than 5s in the prime factorization of n!,
        counting the total number of 5s gives the number of trailing zeros.

        To count the number of 5s in n!:
          1. floor(n / 5)   gives the count of multiples of 5
          2. floor(n / 25)  gives the count of multiples of 25 (each contributes an extra 5)
          3. floor(n / 125) gives the count of multiples of 125 (each contributes yet another 5)
          4. … continue while 5^k ≤ n

        Sum them all up: zeros = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + …

    Examples:
        Input: n = 5
        Output: 1
        Explanation: Factorial of 5 is 120 which has one trailing 0.

        Input: n = 20
        Output: 4
        Explanation: Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.

        Input: n = 100
        Output: 24

"""


# Optimal Approach:

def countTrainlingZeros(number: int) -> int:
    zeros = 0
    power = 5

    # As long as our current power of five (5, 25, 125, 625, …) is ≤ number, we need to count how many multiples of that power fit into number
    while power <= number:
        # n // power_of_five is integer division (also called “floor division”). E.g., 17 // 5 → 3 (because 17 ÷ 5 = 3.4, floored to 3)
        zeros += number // power
        power *= 5
    return zeros



# Naive Approach:
# Complexity Analysis
# Time Complexity: O(n)
# Space Complexity: O(1)
def factorial(number):
    """
       Function to calculate factorial of a number
    """
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact


def countingTrailingZeros(number: int) -> int:
    """
       Function to count trailing zeros in factorial
    """
    fact = factorial(number)
    count = 0

    # Count trailing zeros by dividing the factorial by 10
    while fact % 10 == 0:
        count += 1
        fact //= 10

    return count



if __name__ == "__main__":
    number = int(input("Put your number: "))
    count = countingTrailingZeros(number)
    print(count)

    for x in [7, 17, 100, 1000]:
        print(f"{x}! has {countTrainlingZeros(x)} trailing zero(s)")
