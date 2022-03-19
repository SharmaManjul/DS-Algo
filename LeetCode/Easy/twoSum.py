#Find two elements in list that sum up to the target.

#Brute force: TC=O(n^2) and SC=O(1)
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == target - nums[j] and j != i:
                return [i, j]
