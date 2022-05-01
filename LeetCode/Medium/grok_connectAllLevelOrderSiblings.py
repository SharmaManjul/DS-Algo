from __future__ import print_function
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None
# tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next

def connect_all_siblings(root):
    queue = deque()
    queue.append(root)
    cur_node, prev_node = None, None

    while queue:
        level_len = len(queue)
        for i in range(level_len):
            cur_node = queue.popleft()

            if prev_node:
                prev_node.next = cur_node
            prev_node = cur_node

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    prev_node.next = None
    return root

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()

main()