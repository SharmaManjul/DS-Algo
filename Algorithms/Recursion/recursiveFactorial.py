#Find the factorial using recursion and iteration.

#Recursively
def recursiveFactorial(value): #O(n)
    #Base Case
    if value == 0:
        return 1
    return value * recursiveFactorial(value-1)

print(recursiveFactorial(800))

#Iteratively
def iterativeFactorial(value): #O(2^n)
    factorial = 1
    for i in range(1,value+1):
        factorial *= i
    return factorial

print(iterativeFactorial(800))
