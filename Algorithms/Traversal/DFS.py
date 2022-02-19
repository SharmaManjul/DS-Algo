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
        if not self.root:
            return False
        parentNode = None
        curNode = self.root
        while curNode:
            if value > curNode.value:
                print("curNode to right")
                parentNode = curNode
                curNode = curNode.right
            elif value < curNode.value:
                print("curNode to left")
                parentNode = curNode
                curNode = curNode.left
            elif value == curNode.value:
                print("Value found to remove!")
                #Right of current Node is empty
                if curNode.right == None:
                    if parentNode == None:
                        self.root = curNode.left
                    else:
                        if curNode.value > parentNode.value:
                            parentNode.right = curNode.left
                        elif curNode.value < prevnode.value:
                            parentNode.left = curNode.left
                #Left of right of current node is empty
                elif curNode.right.left == None:
                    print("Made it")
                    curNode.right.left = curNode.left
                    if parentNode == None:
                        self.root = curNode.right
                    else:
                        if curNode.value > parentNode.value:
                            parentNode.right = curNode.right
                        elif curNode.value < parentNode.value:
                            parentNode.left = curNode.right
                else:
                    #Find the right child's leftmost child
                    leftMost = curNode.right.left
                    leftMostParent = curNode.right
                    while leftMost.left is not None:
                        leftMostParent = leftMost
                        leftMost = leftMost.left

                    leftMostParent.left = leftMost.right
                    leftMost.left = curNode.left
                    leftMost.right = curNode.right

                    if parentNode == None:
                        self.root = leftMost
                    else:
                        if curNode.value < parentNode.value:
                            parentNode.left = leftMost
                        elif curNode.value > prevNode.value:
                            parentNode.right = leftMost
                return True

    def dfsInOrder(self):
        return traverseInOrder(self.root, [])

def traverseInOrder(curNode, list):
    print(curNode.value)
    if curNode.left:
        traverseInOrder(curNode.left, list)
    list.append(curNode.value)
    if curNode.right:
        traverseInOrder(curNode.right, list)
    return list

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
print(tree.dfsInOrder())
