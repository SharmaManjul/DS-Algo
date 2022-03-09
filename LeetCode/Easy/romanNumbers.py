#Given input of a string of roman numbers convert to decimal values.

def romanToInt(self, s):
    romanMap = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    num = 0

    for i in range(len(s)-1):
        if romanMap[s[i]] < romanMap[s[i+1]]:
            num -= romanMap[s[i]]
        else:
            num += romanMap[s[i]]
    return num + romanMap[s[-1]]
