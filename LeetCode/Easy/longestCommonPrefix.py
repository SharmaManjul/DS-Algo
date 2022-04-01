#Find longest common string in an array of strings.

#O(total number of characters in the array)
def longestCommonPrefix(self, strs):
    res = ""
    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res