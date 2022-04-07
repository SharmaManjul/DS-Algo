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