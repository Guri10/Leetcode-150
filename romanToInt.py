def romanToInt( s):
    """
    leetcode 13. Roman to Integer
    link: https://leetcode.com/problems/roman-to-integer/
    difficulty: easy

    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    """
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    fin = 0
    for i in range(len(s)):
        if i+1<len(s) and dic[s[i]] < dic[s[i+1]]:
            fin -= dic[s[i]]
        else:
            fin += dic[s[i]]
    return fin


# test cases:
print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))