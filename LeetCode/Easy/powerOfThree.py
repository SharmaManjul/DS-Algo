#Check if number is a power of 3.

#Using while loop with TC=O(n) and SC=O(1)
def isPowerOfThree(self, n):
    power, num = 0, 0
    while True:
        num = 3 ** power
        if n == num:
            return True
        elif n < num:
            return False
        power += 1

