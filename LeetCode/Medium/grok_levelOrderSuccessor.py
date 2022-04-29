from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    def find_successor(root, key):
    # TODO: Write your code here
        return None


def find_successor(root, key):
    queue = deque()
    queue.append(root)
    found_key = 0

    while queue:
        level_len = len(queue)

        for _ in range(level_len):
            cur_node = queue.popleft()

            if found_key == 1:
                return cur_node

            if cur_node.val == key:
                found_key = 1

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)

main()