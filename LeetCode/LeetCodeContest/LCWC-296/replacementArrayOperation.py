# TC = O(N + K) where N is the number of nums and K is the operations.
# SC = O(K)

class Solution(object):
    def arrayChange(self, nums, operations):
        replacements = {}
        # Since we know that the final set value will be in towards the end of the operations we should create a map for
        # the operations backwards so that we can associate the original value to it's final form.
        for x, y in reversed(operations):
            replacements[x] = replacements.get(y, y)

        for n in range(len(nums)):
            if nums[n] in replacements:
                nums[n] = replacements[nums[n]]

        return nums