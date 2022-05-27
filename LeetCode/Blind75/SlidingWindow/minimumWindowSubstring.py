# TC = O(N+M) and SC = O(N+M)
# The target list can be put into a map and we should loop thorugh the s list adding it's elements to its map.
# Once we find an element whose value is the same in both maps then we can increase the have. Once the have and
# need are equal we can store result if it is minimum and pop the leftmost element from the map for s, keep
# popping until have and need are not equal. If the element that we popped is in the target map and the map
# value in s is less than t then we need to reduce our have.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if len(t) == 0 and len(t) > len(s):
            return ""

        t_map, s_map = {}, {}

        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)

        l = 0
        res, res_len = [-1, -1], len(s) + 1
        have, need = 0, len(t_map)
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if res_len < len(s) + 1 else ""