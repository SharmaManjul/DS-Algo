# Maintain aplhabet freq list for the strings and divide the frequencies. Pick the smallest result as the answer.
# TC = O(S+T) and SC = O(26) = O(1)

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_t, freq_s = [0] * 26, [0] * 26
        for char in target:
            freq_t[ord(char) - ord('a')] += 1
        for char in s:
            freq_s[ord(char) - ord('a')] += 1
        res = len(s) + 1
        for char in target:
            res = min(res, freq_s[ord(char) - ord('a')] // freq_t[ord(char) - ord('a')])
        return res if res != len(s) + 1 else 0