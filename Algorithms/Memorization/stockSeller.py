#Brute force approach using loops with T.C. = O(n^2) and S.C O(n). Really bad!
def maxProfit(self, prices):
    diff=[]
    lenP=len(prices)

    if lenP <= 1:
        return 0

    for i in range(lenP):
        for j in range(i+1, lenP):
            diff.append(prices[j]-prices[i])
            
    maxi = max(diff)
    if maxi > 0:
        return maxi
    else:
        return 0

#More efficient approach using single loop T.C. = O(n) and S.C = O(1)
def maxProfit(self, prices):
    maxProfit, buy, sell = 0, 0, 1

    for i in range(len(prices)-1):
        diff = prices[sell] - prices[buy]
        if diff < 0:
            buy = i+1
            sell = i+2
        elif diff >= 0:
            if maxProfit < diff:
                maxProfit = diff
            sell+=1

    return maxProfit
