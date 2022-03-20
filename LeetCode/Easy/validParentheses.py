#Check if given string has valid parentheses.

#TC=O(n) and SC=O(1)
def isValid(self, s):
    stack = []
    validMap = {'(': ')', '{': '}', '[': ']'}
    for p in s:
        if p in validMap.keys():
            stack.append(p)
        elif p in validMap.values():
            if len(stack) == 0 or validMap[stack.pop()] != p:
                return False
        else:
            return False
    return stack == []