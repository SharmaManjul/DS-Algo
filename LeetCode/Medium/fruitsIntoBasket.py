#Same as longest substring with distinct k but k is 2

#TC=O(n) and SC=O(1) because the hashmap will atmost store 3 elements.
def totalFruit(self, str1):
    str_map = {}
    w_start = max_len = 0

    for w_end in range(len(str1)):
        if str1[w_end] in str_map:
            str_map[str1[w_end]] += 1
        else:
            str_map[str1[w_end]] = 1
        while len(str_map) > 2:
            if str_map[str1[w_start]] > 1:
                str_map[str1[w_start]] -= 1
            else:
                del str_map[str1[w_start]]
            w_start += 1
        max_len = max(max_len, w_end - w_start + 1)
    return max_len