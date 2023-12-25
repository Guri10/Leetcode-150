def canJump( nums):
    """
    Leetcode 55: Jump Game
    Leetcode problem number: 55
    Difficulty: Medium
    URL: https://leetcode.com/problems/jump-game/

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position. Determine if you are
    able to reach the last index.
    """
    jump = -float('inf')
    for i in range(len(nums)):
        jump = max(jump, nums[i])
        if i == len(nums)-1:
            return True
        if jump == 0:
            return False
        jump = jump - 1

#test cases
nums = [2,3,1,1,4]
print(canJump(nums))

nums = [3,2,1,0,4]
print(canJump(nums))

