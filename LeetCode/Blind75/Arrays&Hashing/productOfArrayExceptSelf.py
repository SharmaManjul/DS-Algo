# The trick is to first calculate the prev product related to a number and store it in an array and then in the same array
# multiply the calculated next prod associated to a num. Very efficient O(N)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Edge case
        if not nums or len(nums) == 0:
            return []

        result = [1] * len(nums)

        prev_prod = 1
        for index in range(len(nums)):
            result[index] = prev_prod
            prev_prod *= nums[index]

        next_prod = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= next_prod
            next_prod *= nums[index]

        return result