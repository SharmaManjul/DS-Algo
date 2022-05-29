# Uses the concept of monotonic stack which store strictly decreasing nums. So if we reverse loop and check if the cur
# cur num is greater than the smallest element in the stack we increament the steps associated to that index and pop the
# stack. If we pop an element of a stack with a greater step number than the cur index+1 then we should store that step num.
# TC = O(N) and SC = O(N)

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        steps = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                steps[i] = max(steps[i] + 1, steps[stack.pop()])
            stack.append(i)
        return max(steps)