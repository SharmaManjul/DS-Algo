#TC = O(N) and SC= O(1)

def findDuplicate(self, nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

#More readable and slightly more efficient solution.
    def findDuplicate(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1