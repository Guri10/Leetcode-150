
def strStr( haystack, needle):
    """
    leetcode: 28. Implement strStr()
    https://leetcode.com/problems/implement-strstr/
    Difficulty: Easy

    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    """
    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j== len(needle)-1:
                return i
    
    return -1

# test cases
haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))
