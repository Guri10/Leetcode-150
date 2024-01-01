def productExceptSelf(nums):
    """
    leeCode 238. Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/
    difficulty: medium

    Given an array nums of n integers where n > 1,
    return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].


    """
    result = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix 
        prefix *= nums[i]
    # print(result)
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    return result


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([1,2,3,4,5]))