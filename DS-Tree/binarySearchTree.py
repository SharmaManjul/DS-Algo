class Node:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.value = value;

class BinarySearchTree:
    def __init__(self):
        self.root = None;

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            curNode = self.root
            while True:
                if newNode.value < curNode.value:
                    if curNode.left == None:
                        curNode.left = newNode
                        return self
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right == None:
                        curNode.right = newNode
                        return self
                    else:
                        curNode = curNode.right
    def lookup(self, value):
        lookNode = Node(value)
        curNode = self.root
        if (self.root == None):
            print("No tree available")
            return False
        while curNode:
            if lookNode.value > curNode.value:
                curNode = curNode.right
            elif lookNode.value < curNode.value:
                curNode = curNode.left
            else:
                print("Value found in tree!")
                return self
        print("Value not found :(")


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)

tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
printTree(tree.root, 0)
tree.lookup(6)
