#Count the number of trailing zeros in a factorial output given an input.

#Using two loops with a TC = O(m*n) and SC = O(1)
def trailingZeroes(self, n):
    if n < 5:
        return 0
    fact = 1
    zeros = 0

    for i in range(1, n + 1):
        fact *= i

    strFact = str(fact)
    k = len(strFact) - 1

    while strFact[k] == '0':
        zeros += 1
        k -= 1

    return zeros

#Optimized solution by dividing by 5 and its powers. TC = O(log(n)) and SC = O(1)
#TC is actually log(n) base 5 since we had to multiply n fives to get to our solution.
def trailingZeroes(self, n):
    zeros, k = 0, 5
    while k <= n:
        zeros += n // k
        k *= 5
    return zeros