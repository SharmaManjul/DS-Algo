# Using freq_map and finding the max out of all elements in current substring to update res.
# TC = O(26*N) and SC = O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, res = 0, 0
        freq_map = {}

        for end in range(len(s)):
            freq_map[s[end]] = 1 + freq_map.get(s[end], 0)

            if ((end - start + 1) - max(freq_map.values())) > k:
                freq_map[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)

        return res


# Using max_freq to keep track of the most occuring element and updating res based on that.
# TC = O(N) and SC = O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, res = 0, 0
        freq_map = {}
        max_freq = 0

        for end in range(len(s)):
            freq_map[s[end]] = 1 + freq_map.get(s[end], 0)
            max_freq = max(max_freq, freq_map[s[end]])

            if ((end - start + 1) - max(freq_map.values())) > k:
                freq_map[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)

        return res