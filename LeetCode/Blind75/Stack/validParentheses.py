# TC = O(N) and SC = O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets and stack:
                if stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0