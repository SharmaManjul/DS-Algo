nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
  curSum=maxSum=nums[0]

  for item in nums[1:]:
      curSum = max(item, curSum+item)
      maxSum = max(curSum, maxSum)
  return maxSum

print(maxSubArray(nums))
