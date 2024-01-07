def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str

    LeetCode: 14. Longest Common Prefix
    https://leetcode.com/problems/longest-common-prefix/
    difficulty: easy

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    """
    # result = ""
    # for i in range(len(strs[0])):
    #     for s in strs:
    #         if i>=len(s) or s[i] != strs[0][i]:
    #             return result
    #     result += s[i]
    # return result
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

# test cases:
print(longestCommonPrefix(["flower","flow","flight"]))

            