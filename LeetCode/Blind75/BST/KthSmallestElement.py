# Recursive
# TC = O(N) and SC = O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.in_trav(root)
        return self.res

    def in_trav(self, node):
        if not node:
            return
        self.in_trav(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.in_trav(node.right)

# Iterative
# TC = O(N) and SC = O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right