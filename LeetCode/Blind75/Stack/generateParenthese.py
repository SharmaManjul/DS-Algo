# Recursive approach by keeping track of open and close parentheses and using their relation with each other and 'n' to
# decide what to add to result.

# TC = O(2^2N) and SC = O(2N)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def parenthesis_generator(open_num, close_num):
            if open_num == close_num == n:
                res.append("".join(stack))
                return
            if open_num < n:
                stack.append("(")
                parenthesis_generator(open_num + 1, close_num)
                stack.pop()
            if close_num < open_num:
                stack.append(")")
                parenthesis_generator(open_num, close_num + 1)
                stack.pop()

        parenthesis_generator(0, 0)
        return res