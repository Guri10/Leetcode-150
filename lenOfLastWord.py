def lengthOfLastWord( s):
    """
    LeeCode #58
    https://leetcode.com/problems/length-of-last-word/
    difficulty: easy

    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
    return the length of last word (last word means the last appearing word if we loop from left to right) in the string. 
    If the last word does not exist, return 0. Note: A word is defined as a maximal substring consisting of non-space characters only.

    """
    le = 0
    start = len(s)-1
    while s[start] == ' ' and start > -1:
        start -= 1
    while s[start] != ' ' and start > -1:
        le += 1
        start -= 1
    
    return le

# test cases:
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("a "))
print(lengthOfLastWord("   fly me   to   the moon  "))

        


