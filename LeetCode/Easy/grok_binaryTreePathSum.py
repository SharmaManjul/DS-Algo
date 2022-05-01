#Recursively: TC=O(N) since worst case we traverse all the nodes and SC = O(N) to store the recursive stack when tree
# is a linked list.

def hasPathSum(self, root, targetSum):
    if root is None:
        return False

    if root.val == targetSum and root.left is None and root.right is None:
        return True

    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)