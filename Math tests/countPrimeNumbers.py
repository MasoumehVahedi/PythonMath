"""
   Count Prime Numbers

   Question:
        Count how many prime numbers are less than a given non-negative integer n.

    Solution Overview (Sieve of Eratosthenes):
        1. Create a boolean array `is_prime` of length n, initialized to True.
        2. Mark 0 and 1 as non-prime.
        3. For each number p from 2 up to sqrt(n):
             if is_prime[p] is True:
                 mark all multiples of p (from p*p to n, step p) as False.
        4. The remaining True entries correspond to primes. Count them.

    Time Complexity: O(n log log n)
    Space Complexity: O(n)

"""

def findAllPrimes(number: int) -> int:
    """
        Print all prime numbers less than or equal to n, using the Sieve of Eratosthenes.
        """

    # 1. Create a boolean list is_prime[0..n], all initially True
    isPrime = [True] * (number + 1)

    # 2. 0 and 1 are not prime
    if number >= 0:
        isPrime[0] = False
    if number >= 1:
        isPrime[1] = False

    # 3. Sieve: for primeNumber in [2..sqrt(n)], if primeNumber is still prime,
    #    mark all multiples of primeNumber from primeNumber*primeNumber up to number as composite
    primeNumber = 2
    while primeNumber * primeNumber <= number:
        if isPrime[primeNumber]:
            for multiple in range(primeNumber * primeNumber, number + 1, primeNumber):
                isPrime[multiple] = False
        primeNumber += 1

    # 4. Finally, print out all the indices still marked True
    count = 0
    for prime_num in range(2, number + 1):
        if isPrime[prime_num]:
            count += 1
            print(prime_num)

    return count


# Example usage:
if __name__ == "__main__":
    count = findAllPrimes(30)
    print(f"Total prime numbers: {count}")
