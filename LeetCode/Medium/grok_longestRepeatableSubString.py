#Find longest repeatable sub string while replace k characters with anything.

#Trick is to use a hash map to track the frequencies of repeatition and store the max repeatition. Adjust window size if
#the number of distinct items -1 exceeds k and keep checking the max.

#TC=O(n) and SC=O(1) as max you will store is the 26 characters of the alpha.
def characterReplacement(self, s, k):
    w_start = max_l = max_repeat = 0
    freq_map = {}

    for w_end in range(len(s)):
        right = s[w_end]

        if right not in freq_map:
            freq_map[right] = 0
        freq_map[right] += 1

        max_repeat = max(max_repeat, freq_map[right])

        if ((w_end - w_start + 1) - max_repeat) > k:
            left = s[w_start]
            freq_map[left] -= 1
            w_start += 1

        max_l = max(max_l, w_end - w_start + 1)

    return max_l