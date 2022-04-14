#Find min substring that satisfies the pattern.

#Trick is to use a hashmap as a freq tracker and a counter whenever the frequency is reduced until 0. if the matched is
#equal to the len of the pattern then we shrink the windw until not equal, here we also check for min len.

#TC = O(n+m) and SC= O(mg)
def minWindow(self, s, t):
    w_start = s_start = matched = 0
    f_map = {}
    min_len = len(s) + 1

    for item in t:
        if item not in f_map:
            f_map[item] = 0
        f_map[item] += 1

    for w_end in range(len(s)):
        right = s[w_end]

        if right in f_map:
            f_map[right] -= 1
            if f_map[right] >= 0:
                matched += 1

        while matched == len(t):
            if min_len > w_end - w_start + 1:
                min_len = w_end - w_start + 1
                s_start = w_start

            left = s[w_start]
            w_start += 1
            if left in f_map:
                if f_map[left] == 0:
                    matched -= 1
                f_map[left] += 1

    if min_len > len(s):
        return ""
    return s[s_start:s_start + min_len]