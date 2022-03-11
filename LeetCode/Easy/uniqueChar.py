#Find first unique character in string.
#Using hash map with TC=O(n) and SC=O(n)
def firstUniqChar(self, s):
    charMap = dict()
    for i in s:
        if i in charMap:
            charMap[i] += 1
        else:
            charMap[i] = 1

    print(charMap)

    for i in range(len(s)):
        if s[i] in charMap:
            if charMap[s[i]] == 1:
                return i
    return -1
