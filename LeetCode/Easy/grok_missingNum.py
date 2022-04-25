#TC = O(N) + O(N-1) + O(N) => O(N) and SC=O(1)
def missingNumber(self, nums):
    i = 0
    while i < len(nums):
        index_num = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[index_num]:
            nums[i], nums[index_num] = nums[index_num], nums[i]
        else:
            i += 1

    for j in range(len(nums)):
        if j != nums[j]:
            return j

    return len(nums)