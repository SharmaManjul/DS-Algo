nums = [2,5,5,11]
target = 10

def twoSum(nums, target):
        numsMap = dict()

        for i in range(len(nums)):
            if nums[i] not in numsMap:
                comp = target - nums[i]
                numsMap[comp] = i
            else:
                return [numsMap[nums[i]], i]

print(twoSum(nums, target))
