#Traverse Binary tree in format <left><root><right>

#Using recursion: TC=O(n) and SC=O(n)
def inorderTraversal(self, root):
    list = []
    def traverser(root, list):
        if root != None:
            traverser(root.left, list)
            list.append(root.val)
            traverser(root.right, list)
        else:
            return list
    traverser(root, list)
    return list

#Using iteration: TC=O(n) SC=O(n)
def inorderTraversal(self, root):
    stack = []
    res = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right