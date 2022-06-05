# Since goal is to find min number of subsequences we don't have to worry about order.

# TC = O(N*logN) and SC = O(N)

class Solution(object):
    def partitionArray(self, nums, k):
        # Since sorted we dont have to worry about finding max and min.
        nums.sort()
        res = 1
        start = nums[0]
        for num in nums:
            if (num - start) > k:
                res += 1
                start = num
        return res