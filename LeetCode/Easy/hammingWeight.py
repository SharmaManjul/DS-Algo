#Count number of 1s in a 32 bit binary.

#bin function reduces integer to binary and the count function counts the 1.
def hammingWeight(self, n)
    return bin(n).count('1')

#Everytime we AND n and n-1 the result contains one less 1 until it is all zeros. So we can loop and count.
 def hammingWeight(self, n):
    counter = 0
    while n:
        n &= n-1
        counter += 1
    return counter