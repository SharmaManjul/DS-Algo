# TC = O(N*logN) and SC = O(N)

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while len(nums) > 1:
            result = []
            for i in range((len(nums)//2)):
                if i%2 == 0:
                    result.append(min(nums[2*i], nums[2*i+1]))
                else:
                    result.append(max(nums[2*i], nums[2*i+1]))
            print(result)
            nums = result
        return nums[0]