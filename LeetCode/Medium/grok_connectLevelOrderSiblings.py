#TC = O(N) and SC = O(N)

class Solution(object):
    def connect(self, root):
        if root == None:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            level_len = len(queue)
            prev_node = None

            for level_index in range(0, level_len):
                cur_node = queue.popleft()

                if level_index == level_len - 1:
                    cur_node.next == None

                if prev_node:
                    prev_node.next = cur_node
                prev_node = cur_node

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return root