# TC = O(N) and SC = O(N) we need the space for the list and the queue.
def levelOrder(self, root):
    if root == None:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_size = len(queue)
        level_list = []

        for _ in range(level_size):
            cur_node = queue.popleft()
            level_list.append(cur_node.val)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        result.append(level_list)

    return result