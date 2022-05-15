# Using recurssion and top down approach
# TC = O(2^N) and SC = O(N)
class Solution:
    count = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count_sum(nums, target, 0, 0)
        return self.count

    def count_sum(self, nums, target, index, cur_sum):
        if index == len(nums):
            if cur_sum == target:
                self.count += 1
        else:
            self.count_sum(nums, target, index + 1, cur_sum + nums[index])
            self.count_sum(nums, target, index + 1, cur_sum - nums[index])

# Different approach: Looking for a subset with some sum
# The problem can be translated to this equation: S1 - S2 = target but we also know that S1 + s2 = sum(nums) so we get:
# 2*s1 = sum(nums) + target => s1 = (sum(nums) + target) / 2
# So we are looking for a subset with that sum.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # Edge case
        if target > total_sum or (total_sum + target) % 2 != 0:
            return 0

        target_sum = (total_sum + target) // 2

        dp = [[0 for x in range(target_sum + 1)] for y in range(n)]

        # We will always have an empty set for 0 zero sum
        for i in range(n):
            dp[i][0] = 1

        for s in range(1, target_sum + 1):
            if nums[0] == s:
                dp[0][s] = 1
            else:
                dp[0][s] = 0

        # For every index we want to find if the cur sum exists bu either adding the cur num or
        # subtracting the current num.
        for i in range(1, n):
            for s in range(1, target_sum + 1):
                dp[i][s] = dp[i - 1][s]
                if nums[i] <= s:
                    dp[i][s] += dp[i - 1][s - nums[i]]

        return dp[n - 1][target_sum]


#Best solution using recursion top down

# Here the idea is to recursively call a function to find all possible combinations and keep track of the total, We use
# a cache to store results of a particular index and total.

# TC = O(N * T) where N is the number of elements and T is the possible range of sums and SC = O(N * T)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def count_sum(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in cache:
                return cache[(index, total)]
            else:
                cache[(index, total)] = count_sum(index+1, total+nums[index]) + count_sum(index+1, total-nums[index])
                return cache[(index, total)]

        return count_sum(0, 0)
