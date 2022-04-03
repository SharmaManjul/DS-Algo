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

#TC=O(n) and SC=O(1)
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
         if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        elif not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
    return True