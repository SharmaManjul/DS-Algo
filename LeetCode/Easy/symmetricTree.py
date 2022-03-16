#Check if given tree is symmetrical from the middle.

#Recursively using outpair and inpair technique
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return False
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False

#Iteratively using a while loop with TC=O(n) and SC=O(n)
    def isSymmetric(self, root):
        if not root:
            return False
        stack = [(root.left, root.right)]

        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))

        return True