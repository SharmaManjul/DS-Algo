#TC = O(N) and SC=O(N)

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, tree_sum):
        if not node:
            return 0
        #Calculate the the num created from traversal so far.
        tree_sum = 10 * tree_sum + node.val

        #Return num when leaf node
        if not node.left and not node.right:
            return tree_sum

        #Calculate the path nums of left and right sub trees separately and add.
        return dfs(node.left, tree_sum) + dfs(node.right, tree_sum)

    return dfs(root, 0)