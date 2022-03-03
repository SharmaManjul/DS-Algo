#Finding max number of paths to n by taking 1 or 2 steps. There are two decisions
#to make and they are repeated so it is a binary tree and we can DFS to find the
#paths that result in the desiered n. Also used memoization to reduce repeated
#computation.

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
            stepHash[stepSum] = stepCounter(n, stepSum, 1)+stepCounter(n, stepSum, 2)
            return stepHash[stepSum]
    return stepCounter(n, stepSum, step)
