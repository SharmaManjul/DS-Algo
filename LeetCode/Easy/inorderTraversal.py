#Return list with inorder traversal.

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