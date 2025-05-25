"""
   Given a number A, find all factors of A.
   In math, a factor is a number that divides another number completely with no remainder.

   Example Input
    A = 6

   Example Output
    [1, 2, 3, 6]
"""



def allFactors(A):
    result = []

    sqrtA = int(A**0.5)
    for i in range(1, sqrtA + 1):
        if A % i == 0:
            result.append(i)
            # Add the corresponding factor if it's different
            if i != A // 1:
                result.append(A // i)
    return result


if __name__ == "__main__":
    A = 24
    result = allFactors(A)
    print(result)