def trap(height):
    '''
    leetcode 42
    https://leetcode.com/problems/trapping-rain-water/
    difficulty: hard

    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
    
    Two approaches:
    1. Dynamic programming  
        Time complexity: O(n)
        Space complexity: O(n)
        The idea is to store the max height to the left and right of each bar in two arrays. 
        Then, for each bar, the amount of water it can trap is the min of the max height to the left and right minus its own height.

    2. Two pointers
        Time complexity: O(n)
        Space complexity: O(1)
        The idea is to use two pointers to scan from left and right.
        At each step, we compare the max height to the left and right of the two pointers.
        If the max height to the left is smaller, we move the left pointer one step to the right.
        Otherwise, we move the right pointer one step to the left.
        The amount of water that can be trapped at each step is the difference between the max height and the height of the current bar.
        The max height is updated at each step.
        We stop when the two pointers meet.

    '''


    # max_left = [0] * len(height)
    # max_right = [0] * len(height)
    # curr_max = 0
    # for i in range(1,len(height)):
    #     curr_max =  max(height[i-1],curr_max)
    #     max_left[i] = curr_max
    # curr_max = 0
    # for i in range(len(height)-2,-1,-1):
    #     curr_max = max(curr_max,height[i+1])
    #     max_right[i] = curr_max
    # res = 0
    # for i in range(len(height)):
    #     res += max(min(max_left[i],max_right[i])-height[i],0)
    # return res

    max_left=height[0]
    max_right=height[len(height)-1]
    res=0
    i=0
    j=len(height)-1
    while i<j:
        if max_left<=max_right:
            
            i+=1 
            res+= max(max_left-height[i],0)
            max_left=max(height[i],max_left)
            
        else:
           
            j-= 1 
            res+= max(max_right-height[j],0)
            max_right=max(height[j],max_right)
    return res
    



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

