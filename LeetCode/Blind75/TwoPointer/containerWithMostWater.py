# TC = O(N) and SC = O(1)

# We are looking for the maximum area possible, so we are looking for the biggest heights possible. If one of the height
# is smaller than the other adjust it until other wise. Keep checking for area the entire time.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water_amt =
        while l < r:
            max_water_amt = max(max_water_amt, (min(height[l], height[r]) * (r - l)))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water_amt