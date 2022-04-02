#Find is substring exists inside given string.

#TC=O(n*m) and SC=O(1)
def strStr(self, haystack, needle):
    if len(needle) == 0:
        return 0
    ptH, ptN = 0, 0
    while ptH < len(haystack):
        if haystack[ptH] == needle[ptN]:
            if ptN == len(needle) - 1:
                return ptH - ptN
            ptN += 1
        else:
            if ptN > 0:
                ptH = (ptH - ptN)
            ptN = 0
        ptH += 1
    return -1