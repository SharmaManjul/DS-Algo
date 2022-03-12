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
