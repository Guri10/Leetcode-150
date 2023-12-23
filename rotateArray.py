def rotate( nums, k):
    """
    Leetcode problem title: Rotate Array
    Leetcode problem number: 189
    Difficulty: Easy
    URL: https://leetcode.com/problems/rotate-array/

    Given an array, rotate the array to the right by k steps, where k is non-negative.
    """
    k %= len(nums)
    nums.reverse()
    left = 0
    right = k-1
    while (left < right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    left = k
    right = len(nums)-1
    while (left < right):
        temp =  nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    print(nums)


#test cases
nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)

nums = [-1,-100,3,99]
k = 2
rotate(nums,k)
