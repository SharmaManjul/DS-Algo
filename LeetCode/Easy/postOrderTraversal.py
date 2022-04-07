#Traverse Binary tree in format <left><right><root>

#Using recursion: TC=O(n) and SC=O(n)
def postorderTraversal(self, root):
    res = []
    def traverser(root, res):
        if root != None:
            traverser(root.left, res)
            traverser(root.right, res)
            res.append(root.val)
    traverser(root, res)
    return res

#Iteratively: TC=O(n) and SC=O(n)
def postorderTraversal(self, root):
    stack, res = [root], []
     while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
     return res[::-1]