#Find out if the given two strings are anagrams.
#Iterative approach using hash maps with TC=O(n) and SC=O(n)

def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    wordMap = dict()
    for i in range(len(s)):
        if s[i] in wordMap:
            wordMap[s[i]] += 1
        else:
            wordMap[s[i]] = 1

    for j in range(len(t)):
        if t[j] in wordMap:
            wordMap[t[j]] -= 1
            if wordMap[t[j]] < 0:
                return False
        else:
            return False
    return True
