def maxProfit( prices):
    """
    122. Best Time to Buy and Sell Stock II
    Easy
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    Say you have an array prices for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many transactions as you
    like (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the
    stock before you buy again).

    """
    i,j=0,1
    profit=0
    for j in range(1,len(prices)):
        if prices[i]<prices[j]:
            profit += prices[j]-prices[i]
        i=j
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [1,2,3,4,5]
print(maxProfit(prices))
