def jump(nums):
    '''
    Leetcode 45: Jump Game II
    Leetcode problem number: 45
    Difficulty: Hard
    URL: https://leetcode.com/problems/jump-game-ii/

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position. Your goal is to reach
    the last index in the minimum number of jumps.

    '''
    n = len(nums)
    if n <= 1:
        return 0

    # The max position one can reach from the current position
    max_reach = nums[0]
    # The number of steps one can still take before needing to jump again
    steps = nums[0]
    # Number of jumps needed
    jumps = 1

    for i in range(1, n):
        # If the current index is beyond the maximum reachable index, then jump
        if i > max_reach:
            jumps += 1
            max_reach = steps
        steps = max(steps, i + nums[i])

    return jumps

#test cases
nums = [2,3,1,1,4]
print(jump(nums))

nums = [3,2,1,0,4]
print(jump(nums))