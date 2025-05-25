"""
    Excel Column Number:
    Given a column title A as appears in an Excel sheet, return its corresponding column number.

    Problem Constraints
    1 <= |A| <= 100

    Input Format
    First and only argument is string A.

    Output Format
    Return an integer

    Example Input
    Input 1:
     "A"
    Input 2:

     "AB"

    Example Output
    Output 1:
     1
    Output 2:
     28

    Example Explanation
    Explanation 1:
        A -> 1
    Explanation 2:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28


    Solution:
    We need to convert Excel column titles to numbers. This is essentially a base-26 number system where A=1, B=2, ..., Z=26.
    Let us trace through the examples:
        - "A" = 1
        - "AB" = A×26¹ + B×26⁰ = 1×26 + 2×1 = 28

"""


def excelToNumber(A):
    # @param A : string
    # @return an integer

    result = 0
    for char in A:
        # Convert char to number (A=1, B=2, ..., Z=26)
        digit_val = ord(char) - ord("A") + 1
        # Shift previous result and add current digit
        result = result * 26 + digit_val
    return result



# Now, convert an integer into excel column title.
# Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
def convertToTitle(A):
    # @param A : integer
    # @return a strings
    result = ""
    while A > 0:
        A -= 1    # Subtract 1 to make it 0-based for modulo operation
        char = chr(ord("A") + A % 26)  # Get the character (A=0, B=1, ..., Z=25)
        result = char + result
        A //= 26    # Move to next position
    return result



if __name__ == "__main__":
    A = "AB"
    result = excelToNumber(A)
    print(result)

    A = 28
    char = convertToTitle(A)
    print(char)