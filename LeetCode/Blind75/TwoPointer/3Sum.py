# TC = O(N^2) + O(NlogN) = O(N^2) and SC = O(N) due to sorting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # We need to sort the array so we can divide the problem into looping through and perfomring two sum on the rest.
        nums.sort()

        for i, num in enumerate(nums):
            # Handle the case when next element is same as the prev, so to prevent duplicates increament until new not equal
            # to old.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # The value we wan to perform two sum is num.
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                else:
                    # Successfully found one possible result but we need ot keep going until l < r. But there is a possibility of
                    # encountering same values which will lead to duplicate results. To handle that we only need to move either
                    # l or r to an element that is unique and the conditions above will take care of the rest.
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res