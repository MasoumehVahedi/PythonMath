"""
   Happy Number

    Question:
        Write an algorithm to determine if a number n is "happy".
        Return True if n is a happy number, and False if not.

    Solution Overview:
        A happy number is defined by the following process:
          1. Given a number n, generate its “next” number by squaring each of its digits and summing the results.
             e.g. next(19) = 1^2 + 9^2 = 82.
          2. Repeat this process in a loop.
          3. If you eventually reach 1, n is happy → return True.
          4. If you enter a cycle that never reaches 1 (i.e. you see the same number twice), n is unhappy → return False.

        Implementation Details:
          • Use integer division and modulus (//, %) to extract each digit.
          • Keep a set of seen intermediate sums; if a sum repeats, we have a cycle.
"""


def getNextNumber(number: int) -> int:
    sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        sum += digit * digit
    return sum


def isHappy(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = getNextNumber(number)
    return number == 1


if __name__ == "__main__":
    number = int(input("Put your number: "))
    happy = isHappy(number)
    print(happy)



