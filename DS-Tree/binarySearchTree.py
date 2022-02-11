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
                print("Value found!")
                return self
        print("Value not found :(")

    def remove(self, value):
        removeNode = Node(value)
        prevNode = Node(None)
        curNode = self.root
        if (self.root == None):
            print("No tree available")
            return False
        while curNode:
            if removeNode.value > curNode.value:
                prevNode = curNode
                curNode = curNode.right
            elif removeNode.value < curNode.value:
                prevNode = curNode
                curNode = curNode.left
            elif removeNode.value == curNode.value:
                #Right of current Node is empty
                if curNode.right == None:
                    if prevNode == None:
                        self.root = curNode.left
                    else:
                        if curNode.value > prevNode.value:
                            prevNode.right = curNode.left
                        elif curNode.value < prevnode.value:
                            prevNode.left = curNode.left
                #Left of right of current node is empty
                elif curNode.right.left == None:
                    curNode.right.left = curNode.left
                    if prevNode == None:
                        self.root = curNode.right
                    else:
                        if curNode.value > prevNode.value:
                            prevNode.right = curNode.right
                        elif curNode.value < prevnode.value:
                            prevNode.left = curNode.right
                else:
                    #Find the right child's leftmost child
                    leftMost = curNode.right.left
                    leftMostParent = curNode.Right
                    while leftMost.left is not None:
                        leftMostParent = leftMost
                        leftMost = leftMost.left

                    leftMostParent.left = leftMost.right
                    leftMost.left = curNode.left
                    leftMost.right = curNode.Right

                    if prevNode == None:
                        self.root = leftMost
                    else:
                        if curNode.value < prevNode.value:
                            prevNode.left = leftMost
                        elif curNode.value > prevNode.value:
                            prevNode.right = leftMost

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
tree.remove(6)
printTree(tree.root, 0)
