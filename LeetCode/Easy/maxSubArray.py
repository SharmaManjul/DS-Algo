#Return maximum sum of continuous items in the array.

#With two variable curSum and maxSum, TC=O(n) and SC=O(n)
def maxSubArray(self, nums):
    curSum = maxSum = nums[0]

    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(curSum, maxSum)
    return maxSum