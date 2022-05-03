#TC=O(N) and SC=O(N)

def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
    def sequence_checker(node, path_arr, s_index):
        if not node:
            return False
        #Check if exceed arr lenght or elements not equal.
        if s_index >= len(arr) or arr[s_index] != node.val:
            return False
        #Check if leaf node and len of arr is equal to index.
        if not node.left and not node.right and s_index == len(arr) - 1:
            return True

        return sequence_checker(node.left, path_arr, s_index + 1) or sequence_checker(node.right, path_arr, s_index + 1)

    return sequence_checker(root, [], 0)