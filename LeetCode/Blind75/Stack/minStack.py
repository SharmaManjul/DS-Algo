# Trick is to use an additional stack to store mins seen so far with the smallest min being at the end of the list.
# TC = O(1) and SC = O(N)

class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.stack_min[-1]:
            self.stack_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()