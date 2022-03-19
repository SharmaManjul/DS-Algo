#House Robber

#Recursively calling two options and checking max. Very bad time complexity: TC=O(2^n) and SC=O(n)
def rob(self, nums):
    def robbing(nums, i):
        return max(robbing(nums, i + 1), nums[i] + robbing(nums, i + 2)) if i < len(nums) else 0
    return robbing(nums, 0)

#Using a simple loop and two vars to keep track of current and possible maxes.
def rob(self, nums):
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2