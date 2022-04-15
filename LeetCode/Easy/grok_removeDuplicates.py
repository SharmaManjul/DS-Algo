#Remove duplicates in place and return the length of the new string.

#TC = O(N) and O(1)

def removeDuplicates(self, nums):
    duplicate = 1

    for i in range(len(nums)):
        if nums[duplicate - 1] != nums[i]:
            nums[duplicate] = nums[i]
            duplicate += 1

    return duplicate