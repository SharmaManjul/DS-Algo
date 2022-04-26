#TC=O(N) and SC=(1)

#Trick is to perform cyclic sort only within the range 1 to n and not care about the rest as the rest will populate the
# missing element and the first incorrect field we encounter after sorting will be the min positive num. Remember 0 is
#not a positive number.

def firstMissingPositive(self, nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] >= 0 and nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
