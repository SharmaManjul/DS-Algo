# TC = O(N) and SC = O(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_input = ""
        for char in s:
            if char.isalnum():
                normalized_input += char.lower()
        start = 0
        for end in range(len(normalized_input) - 1, (len(normalized_input) // 2) - 1, -1):
            if normalized_input[end] != normalized_input[start]:
                return False
            start += 1
        return True