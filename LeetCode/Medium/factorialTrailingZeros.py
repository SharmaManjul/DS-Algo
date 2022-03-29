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