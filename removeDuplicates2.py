def removeDuplicates(nums):
    """
    Leetcode problem title: Remove Duplicates from Sorted Array II
    Leetcode problem number: 80
    Difficulty: Medium
    URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

    Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    """
    i,j = 2,2
    while j < len(nums):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
        j+=1
    return i

#test cases
nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
