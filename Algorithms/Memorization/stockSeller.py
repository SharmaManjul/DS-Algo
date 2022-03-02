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
