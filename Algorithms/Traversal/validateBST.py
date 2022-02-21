# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Function to recursively call itself while checking for lower and upper bounds
        def validator(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return validator(node.left, left, node.val) and validator(node.right, node.val, right)

        return validator(root, float("-inf"), float("inf"))
