#Converted a given sorted ascending list to a height balanced BST.

#Used recursion to solve this probelm but finding the mid and a base condition
#of left never being greater than right.

class Solution(object):
    def sortedArrayToBST(self, nums):
        def treeBuilder(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = treeBuilder(left, mid-1)
            root.right = treeBuilder(mid+1, right)
            return root

        return treeBuilder(0, len(nums)-1)
