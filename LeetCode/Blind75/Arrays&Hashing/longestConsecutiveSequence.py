class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # In every sequence the starting number does not have the number before it in the list.
        # So we need to find this starting num in the array and when we do we need keep tracking
        # len of this sequence by checking the num+1 exists.

        num_set = set(nums)
        seq_len = 0

        for num in nums:
            if num - 1 not in num_set:
                cur_len = 0
                while num + cur_len in num_set:
                    cur_len += 1
                seq_len = max(seq_len, cur_len)

        return seq_len
