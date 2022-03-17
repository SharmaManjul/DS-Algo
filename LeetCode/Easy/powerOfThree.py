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

#We know the max integer possible that is a power of 3 is 1162261467 so the modulus with n if n is a power of 3 will always be 0.
#TC=O(1) and SC=O(1)
def isPowerOfThree(self, n):
    return n > 0 and 1162261467 % n == 0