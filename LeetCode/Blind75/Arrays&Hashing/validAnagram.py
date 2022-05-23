# Create hash map for both the words and check if counts are equal.
# TC = O(N) and SC = O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()

        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1

        for char in t:
            if char in s_map:
                s_map[char] -= 1
            else:
                return False

        for char in s_map:
            if s_map[char] != 0:
                return False

        return True