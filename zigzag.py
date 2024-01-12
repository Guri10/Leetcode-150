def convert( s, numRows):
    """
    Leetcode 6. ZigZag Conversion
    https://leetcode.com/problems/zigzag-conversion/
    Difficulty: Medium

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    """
    if numRows == 1:
        return s
    res = ""
    for row in range(numRows):
        increment = 2 * (numRows-1)
        for i in range(row, len(s), increment):
            res += s[i]
            if (0 < row < numRows-1) and ((i + increment - 2*row) < len(s)):
                res += s[i + increment - 2*row]

    return res

# test cases
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))

s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
