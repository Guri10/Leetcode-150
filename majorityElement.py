def majorityElement( nums):
    """
    Leetcode problem title: Majority Element
    Leetcode problem number: 169
    Difficulty: Easy
    URL: https://leetcode.com/problems/majority-element/

    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.
    """
    dic = {}
    maxi = 0
    maxi_ele = 0
    for ele in nums:
        if ele not in dic:
            dic[ele]=1
        else:
            dic[ele]+=1
    for key,value in dic.items():
        if value>len(nums)/2 and value>maxi:
            maxi = value
            maxi_ele = key
    return maxi_ele

#test cases
nums = [3,2,3]
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
