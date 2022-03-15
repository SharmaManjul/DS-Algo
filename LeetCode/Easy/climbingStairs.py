#Compute number of ways it is possible to climb staircase with fixed height in increments of 1 or 2.

#Using recursion and memoization with hashMap
def climbStairs(self, n):
    stepSum = 0
    step = 0
    stepHash = dict()

    def stepCounter(n, stepSum, step):
        stepSum += step
        if stepSum in stepHash:
            return stepHash[stepSum]
        else:
            if stepSum == n:
                return 1
            elif stepSum > n:
                return 0
            stepHash[stepSum] = stepCounter(n, stepSum, 1) + stepCounter(n, stepSum, 2)
            return stepHash[stepSum]

    return stepCounter(n, stepSum, step)