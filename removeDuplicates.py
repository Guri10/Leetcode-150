def removeDuplicates(nums):
    """
    Leetcode problem title: Remove Duplicates from Sorted Array
    Leetcode problem number: 26
    Difficulty: Easy
    URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    """
    i,j=0,1
    for j in range(len(nums)):
        if nums[i]==nums[j]:
            j+=1
        else:
            i+=1
            nums[i] = nums[j]
            j+=1
    return i+1
    

#test cases
nums = [1,1,2]
print(removeDuplicates(nums))

nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))