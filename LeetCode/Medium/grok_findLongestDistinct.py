#Find longest distinct substring

#Use a hash map to keep track of all characters and their indexes. When repeat character found check if start is bigger
#than index+1 if it is then old character else two repeat characters after start so move start to index+1

#TC=O(n) and SC=O(n) but SC is better represented as O(1) since max storage will be the 26 characters of the alpha!
def lengthOfLongestSubstring(self, s):
    window_start = current_max = 0
    char_map = {}

    for window_end in range(len(s)):
        right_item = s[window_end]

        if right_item in char_map:
            window_start = max(window_start, char_map[right_item] + 1)

        char_map[right_item] = window_end
        current_max = max(current_max, window_end - window_start + 1)

    return current_max