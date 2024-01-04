def candy(ratings):
    """
    leetcode 135. Candy
    https://leetcode.com/problems/candy/
    difficulty: hard

    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

    """
    n = len(ratings)
    if n == 0:
        return 0

    dic = [1] * n  # Initialize all candy counts to 1

    # Forward pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            dic[i] = dic[i - 1] + 1

    # Backward pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            dic[i] = max(dic[i], dic[i + 1] + 1)

    res = sum(dic)
    return res


print(candy([1, 2, 3, 4]))
print(candy([1,2,2]))
print(candy([1,0,2]))


