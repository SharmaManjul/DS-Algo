# Maintain a stack to get latest two elements to perform operation and add back the element for future operations.
# TC = O(N) and SC = O(N)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                second_num, first_num = stack.pop(), stack.pop()
                stack.append(first_num - second_num)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                second_num, first_num = stack.pop(), stack.pop()
                stack.append(int(first_num / second_num))
            else:
                stack.append(int(token))
        return stack.pop()
