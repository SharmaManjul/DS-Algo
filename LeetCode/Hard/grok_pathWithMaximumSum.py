#TC = O(N) and SC = O(N)

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.max_sum = -1001
    def max_sum_finder(node):
        if not node:
            return 0

        #Get max possible sum from left and right sub trees.
        l_sum = max_sum_finder(node.left)
        r_sum = max_sum_finder(node.right)

        #Ensure that the left or right sum is not negative and if it is then set to 0. Since negative added together result
        #only in smaller numbers.
        l_sum = max(l_sum, 0)
        r_sum = max(r_sum, 0)

        #calculate the current sum with left, right and current node value.
        cur_sum = l_sum + r_sum + node.val

        #Check if current sum is the maximum.
        self.max_sum = max(self.max_sum, cur_sum)

        #Return the path with the maximum sum.
        return max(l_sum, r_sum) + node.val

    max_sum_finder(root)
    return self.max_sum