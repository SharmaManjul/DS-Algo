#House Robber

#Recursively calling two options and checking max. Very bad time complexity: TC=O(2^n) and SC=O(1)
def rob(self, nums):
    def robbing(nums, i):
        return max(robbing(nums, i + 1), nums[i] + robbing(nums, i + 2)) if i < len(nums) else 0
    return robbing(nums, 0)