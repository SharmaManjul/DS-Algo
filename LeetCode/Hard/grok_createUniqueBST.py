# TC = O(N * 2^N) and SC = O(2^N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return []
        # Calling tree finder for all possible BST in range 1 to n
        return self.tree_finder(1, n)

    def tree_finder(self, start, end):
        result = []

        if start > end:
            result.append(None)
            return result

        for root_node in range(start, end + 1): #O(N)
            # Find all possible left sub trees for root_node.
            left_tree = self.tree_finder(start, root_node - 1) # O(2^N)
            # Find all possible right sub trees for root_node.
            right_tree = self.tree_finder(root_node + 1, end)

            # Add all combinations of left and right subtrees to the result
            for left in left_tree:
                for right in right_tree:
                    root = TreeNode(root_node, left, right)
                    result.append(root)

        return result
