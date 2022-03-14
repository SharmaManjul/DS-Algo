#Check if given number is a happy number.

#Algo has TC=O(log n) and SC=O(log n)
def isHappy(self, n):
    squaredMap = dict()
    squared = 0
    while True:
        squared = 0
        while n:
            digit = n % 10
            squared += digit * digit
            n /= 10
        if squared == 1:
            return True
        else:
            if squared in squaredMap:
                return False
            squaredMap[squared] = True
            n = squared