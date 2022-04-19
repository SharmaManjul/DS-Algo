#Trick is to first find invalid subarray and then find the min and max of that array. If any element on the left are more
#than the min and if any elements are less than the max on the right then include them.

#TC=O(N) and SC=O(1)
def findUnsortedSubarray(self, nums):
    left, right = 0, len(nums) - 1

    while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
        left += 1

    if left == len(nums) - 1:  # List is already sorted.
        return 0

    while right > 0 and nums[right - 1] <= nums[right]:
        right -= 1

    sub_min = min(nums[left:right + 1])
    sub_max = max(nums[left:right + 1])

    # Check is anything less than min on the left side.
    while left > 0 and nums[left - 1] > sub_min:
        left -= 1

    # Check is anything more than max on the right side.
    while right < len(nums) - 1 and nums[right + 1] < sub_max:
        right += 1

    return right - left + 1