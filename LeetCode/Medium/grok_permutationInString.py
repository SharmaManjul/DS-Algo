#Find out if permutation of a string exists in given string.

#Trick is to use hash map to store frequency of the permutation string and add to counter whenever you encounter the element
#in the real string, return true when counter == len of map and keep adjusting window length by checking if end - start is
#equal to permutation string.

#TC= O(n+m) n&m are lengths of the two strings and SC=O(26)
def checkInclusion(self, s1, s2):
    w_start = counter = 0
    w_map = {}

    for item in s1:
        if item not in w_map:
            w_map[item] = 0
        w_map[item] += 1

    for w_end in range(len(s2)):
        right = s2[w_end]

        if right in w_map:
            w_map[right] -= 1
            if w_map[right] == 0:
                counter += 1

        if counter == len(w_map):
            return True

        if w_end >= len(s1) - 1:
            left = s2[w_start]
            w_start += 1
            if left in w_map:
                if w_map[left] == 0:
                    counter -= 1
                w_map[left] += 1
    return False