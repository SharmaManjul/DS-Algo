#Return first index of all anagrams in the string of given pattern.

#Same idea but instead of returning true just add window_start to a list and return the list.

#TC=O(n+m) and SC = O(m + k)
def findAnagrams(self, s, p):
    w_start = counter = 0
    w_map = {}
    indexes = []

    for item in p:
        if item not in w_map:
            w_map[item] = 0
        w_map[item] += 1

    for w_end in range(len(s)):
        right = s[w_end]

        if right in w_map:
            w_map[right] -= 1
            if w_map[right] == 0:
                counter += 1

        if counter == len(w_map):
            indexes.append(w_start)

        if w_end - w_start + 1 >= len(p):
            left = s[w_start]
            w_start += 1
            if left in w_map:
                if w_map[left] == 0:
                    counter -= 1
                w_map[left] += 1

    return indexes