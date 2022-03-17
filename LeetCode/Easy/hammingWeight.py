#Count number of 1s in a 32 bit binary.

#bin function reduces integer to binary and the count function counts the 1.
def hammingWeight(self, n)
    return bin(n).count('1')