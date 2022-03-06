#Find max tree depth. Done using recursion and dfs with TC: O(n) and SC: O(1) but
#O(n) with recursive space in mind.

def maxDepth(self, root):
    def depthFinder(root, depth):
        if not root:
            return depth
        return max(depthFinder(root.left, depth+1), depthFinder(root.right, depth+1))
    return depthFinder(root, 0)
