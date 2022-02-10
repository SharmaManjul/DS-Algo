class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.first.value

    def enqueue(self, value):
        if self.length == 0:
            self.first = Node(value)
            self.last = self.first
            self.length = 1
        else:
            newElement = Node(value)
            self.last.next = newElement
            self.last = newElement
            self.length +=1

    def dequeue(self):
        if self.length == 0:
            return "Error stack empty"
        elif(self.first == self.last):
            self.last = None
        else:
            self.first = self.first.next
            self.length -=1


    def printl(self):
        temp = self.first
        while temp != None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))

  #isEmpty

myStack = Stack()
myStack.enqueue("google")
myStack.enqueue("poogle")
myStack.enqueue("myspace")
myStack.enqueue("amz")
print(myStack.peek())
myStack.printl()
myStack.dequeue()
myStack.printl()
myStack.dequeue()
myStack.printl()
