#TC = O(N) + O(N-1) + O(N) => O(N) and SC= O(1)

def findDisappearedNumbers(self, nums):
    i = 0
    missing_nums = []

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_nums.append(i + 1)

    return missing_nums