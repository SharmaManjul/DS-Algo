#Calculate the min size subarray that equals target.

#Using the Sliding window method with TC = O(N) and SC=O(1)g
def minSubArrayLen(self, target, nums):
    w_start = w_sum = 0
    w_min = len(nums) + 1

    for w_end in range(len(nums)):
        w_sum += nums[w_end]

        while w_sum >= target:
            w_min = min(w_min, w_end - w_start + 1)
            w_sum -= nums[w_start]
            w_start += 1

    if w_min == len(nums) + 1:
        return 0
    else:
        return w_min