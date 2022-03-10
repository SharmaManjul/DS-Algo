#Iterative solution using a for loop with TC:O(n) and SC:O(1)
def maxProfit(self, prices):
    maxProfit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            maxProfit += prices[i+1] - prices[i]
    return maxProfit
