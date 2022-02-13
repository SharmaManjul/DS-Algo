class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.top.value

    def push(self, value):
        if self.length == 0:
            self.top = Node(value)
            self.bottom = self.top
            self.length = 1
        else:
            newElement = Node(value)
            newElement.next = self.top
            self.top = newElement
            self.length +=1

    def pop(self):
        if self.length == 0:
            return "Error stack empty"
        else:
            self.top = self.top.next
            self.length -=1


    def printl(self):
        temp = self.top
        while temp != None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))

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
