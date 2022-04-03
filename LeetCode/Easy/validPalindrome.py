#Check if valid palindrome only for alphanumrical.

#TC=O(n) and SC=O(n)
def isPalindrome(self, s):
    s = s.lower()
    p = []
    for char in s:
        if char.isalnum():
            p.append(char)
    j = len(p) - 1
    for i in range(len(p) / 2):
        if p[i] != p[j]:
            return False
        j -= 1
    return True