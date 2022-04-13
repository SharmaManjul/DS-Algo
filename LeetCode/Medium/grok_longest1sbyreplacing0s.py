#Trick here is track number of 1s with a varible and check is window lenght - num of 1s is more than k and then adjust.

#TC=O(n) and SC=O(1)
def longestOnes(self, nums, k):
    w_start = max_l = num_of_1 = 0

    for w_end in range(len(nums)):
        r = nums[w_end]

        if r == 1:
            num_of_1 += 1

        if (w_end - w_start + 1) - num_of_1 > k:
            r = nums[w_start]
            if r == 1:
                num_of_1 -= 1
            w_start += 1

        max_l = max(max_l, w_end - w_start + 1)

    return max_l