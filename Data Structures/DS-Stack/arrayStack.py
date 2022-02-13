#Implementing stacks using arrays is more simpler that linked list as array are
#already kind of like stacks as a data structure.

class Stack:
    def __init__(self):
        self.stackArray = []

    def peek(self):
        arrayLen = len(self.stackArray)
        return self.stackArray[arrayLen-1]

    def push(self, value):
        self.stackArray.append(value)

    def pop(self):
        self.stackArray.pop()


    def printl(self):
        print(self.stackArray)
  #isEmpty

myStack = Stack()
myStack.push("google")
myStack.push("poogle")
myStack.push("myspace")
myStack.push("amz")
print(myStack.peek())
myStack.printl()
myStack.pop()
myStack.printl()
