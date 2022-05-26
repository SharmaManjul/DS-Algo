# TC = O(N) and SC = O(N)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            cur_list = [left + 1, right + 1]
            if cur_sum == target:
                return cur_list
            elif cur_sum > target:
                right -= 1
            else:
                left += 1