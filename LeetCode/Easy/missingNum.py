#Finding the missing num in given list.

#Brute force with TC=O(nlog(n)) and SC=O(1)
def missingNumber(self, nums):
    n = len(nums)
    nums.sort()
    if nums[n-1] != n:
        return n
    for i in range(n-1):
        if nums[i]+1 != nums[i+1]:
            return nums[i]+1
    return 0

#optimized approach using total sum subtraction with TC=O(2n) and SC=O(1)
def missingNumber(self, nums):
    res = 0
    for i in range(len(nums)):
        res += (i - nums[i])
    return res+i+1

#Best approach using XOR and bit manipulation with TC=O(n) and SC=O(1)
def missingNumber(self, nums):
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ i ^ nums[i]
    return xor^i+1
