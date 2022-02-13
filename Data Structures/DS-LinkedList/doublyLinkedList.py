#Making a doubly linked list in python using a class and helper methods to support
#the linked list functionality
#Directory:
#1. Self is the same as this in java
#2. __init__ is a constructor
#3. None is null

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, item):
        newNode = Node(item)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1

    def prepend(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, item):
        newNode = Node(item)
        if index == 0:
            self.prepend(item)
            return
        if index >= self.length:
            self.append(item)
            return
        curNode = self.traverseToIndex(index)
        newNode.next = curNode
        previous = curNode.prev
        newNode.prev = previous
        previous.next = newNode
        self.length+=1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -=1
            return
        if index > self.length or index < 0:
            print("Outside the bounds of the linked list, choose another index.")
            return

        curNode = self.traverseToIndex(index)
        previous = curNode.prev
        successor = curNode.next
        previous.next = successor
        successor.prev = previous
        self.length -=1


    def traverseToIndex(self, index):
        counter = 0
        curNode = self.head
        while counter is not index:
            curNode = curNode.next
            counter+=1
        return curNode

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))

myLinkedList = LinkedList(10)
myLinkedList.append(2)
myLinkedList.prepend(43)
myLinkedList.insert(0, 89)
myLinkedList.insert(10, 55)
myLinkedList.insert(3, 67)
myLinkedList.printl()
myLinkedList.remove(3)
myLinkedList.printl()
