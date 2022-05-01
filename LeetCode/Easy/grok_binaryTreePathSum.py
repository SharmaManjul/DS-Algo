#Recursively: TC=O(N) since worst case we traverse all the nodes and SC = O(N) to store the recursive stack when tree
# is a linked list.

def hasPathSum(self, root, targetSum):
    if root is None:
        return False

    if root.val == targetSum and root.left is None and root.right is None:
        return True

    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

#Iteratively: TC =O(N) and SC=O(N)

    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        stack = [(root, root.val)]

        while stack:

            cur, val = stack.pop()

            if not cur.left and not cur.right and val == targetSum:
                return True

            if cur.right:
                stack.append((cur.right, val + cur.right.val))
            if cur.left:
                stack.append((cur.left, val + cur.left.val))

        return False