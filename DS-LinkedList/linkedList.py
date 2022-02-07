#Making a linked list in python using a class and helper methods to support
#the linked list functionality
#Directory:
#1. Self is the same as this in java
#2. __init__ is a constructor
#3. None is null

class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1
        print(self.head, self.tail, self.length)

myLinkedList = LinkedList(10)
print(myLinkedList)
