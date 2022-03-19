#Find two elements in list that sum up to the target.

#Brute force: TC=O(n^2) and SC=O(1)
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == target - nums[j] and j != i:
                return [i, j]

#Using hashmap to store all compliments with TC=O(n) and SC=O(n)
def twoSum(self, nums, target):
    numsMap = dict()
    for i in range(len(nums)):
        if nums[i] in numsMap:
            return [i, numsMap[nums[i]]]
        else:
            numsMap[target - nums[i]] = i
