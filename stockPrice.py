def maxProfit(prices):
    '''
    121. Best Time to Buy and Sell Stock
    Easy
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell
    one share of the stock), design an algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.

    1. Brute Force
    Time complexity: O(n^2)
    Space complexity: O(1)
    2. One Pass
    Time complexity: O(n)
    Space complexity: O(1)


    '''
    # profit = 0
    # i,j=0,1
    # for i in range(len(prices)):
    #     for j in range(i+1,len(prices)):
    #         if prices[i]<prices[j] and profit < (prices[j]-prices[i]):
    #             profit = prices[j]-prices[i]
    # return profit
    i,j=0,1
    profit = 0
    while j< len(prices):
        curProf = prices[j]-prices[i]
        if prices[j]>prices[i]:
            profit = max(curProf, profit)
        else:
            i=j
        j+=1
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))


