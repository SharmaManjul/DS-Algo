# Use hash map to store the complement and check if complement exists while looping through the array.
# TC = O(N) and SC = O(N)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    complements = dict()
    for i in range(len(nums)):
        if nums[i] in complements:
            return [complements[nums[i]], i]
        else:
            complements[target - nums[i]] = i