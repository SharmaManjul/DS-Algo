class MyQueue(object):

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.pushStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[len(self.popStack)-1]


    def empty(self):
        """
        :rtype: bool
        """
        return (not self.popStack) and (not self.pushStack)




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
