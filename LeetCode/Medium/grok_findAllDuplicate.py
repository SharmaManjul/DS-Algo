#TC = O(N) and SC=O(N)

def findDuplicates(self, nums):
    i = 0
    result = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(nums[i])

    return result