#Traverse Binary tree in format <root><left><right>

#Using recursion: TC=O(n) and SC=O(n)
def preorderTraversal(self, root):
    res = []
    def traverser(root, res):
        if root != None:
            res.append(root.val)
            traverser(root.left, res)
            traverser(root.right, res)
    traverser(root, res)
    return res

#Iteratively: TC=O(n) and SC=O(n)
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res