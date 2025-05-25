"""
   Sorted permutation rank
    Given a string, find the rank of the string amongst its permutations sorted lexicographically. Assume that no characters are repeated.

    Example :
    Input : 'acb' Output : 2
    The order permutations with letters 'a', 'c', and 'b' :
        abc
        acb
        bac
        bca
        cab
        cba
    The answer might not fit in an integer, so return your answer % 1000003

"""

MOD = 1_000_003

def factorial(number: int) -> int:
    """Calculate factorial of n with modulo"""
    if number == 0:
        return 1
    else:
        return (number * factorial(number - 1)) % MOD



def findRank(s: str) -> str:
    """
        Find the rank of string A amongst its permutations sorted lexicographically.

        Args:
            A (str): Input string with no repeated characters

        Returns:
            int: Rank of the string (1-indexed) modulo 1000003
    """
    ans = 0
    n = len(s)
    # For each position, count how many smaller characters come after it
    for i in range(n - 1):
        count = 0
        # Count characters smaller than s[i] that appear after position i
        for j in range(i + 1, n):
            if s[j] < s[i]:
                count += 1

        # Add contribution to rank: count * (n-i-1)!
        ans += (count * factorial(n - i - 1)) % MOD
        ans %= MOD

    return (ans + 1) % MOD


if __name__ == "__main__":
    # Test case from the problem
    test_string = "acb"
    result = findRank(test_string)
    print(f"Input: '{test_string}'")
    print(f"Rank: {result}")

    # Additional test cases
    test_cases = ["abc", "bac", "cab", "cba"]
    print("\nAll permutations of 'abc' and their ranks:")
    for test in test_cases:
        rank = findRank(test)
        print(f"'{test}' -> Rank: {rank}")











"""
   Sorted permutation rank with repeats

   Question
    Given a string, find the 1-based rank of the string among all its unique permutations
    when they are sorted lexicographically (by ASCII order).

    Note: Characters may repeat, so duplicate permutations are not counted multiple times.




"""