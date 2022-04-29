# TC = O(N) and SC = O(N) we need the space for the list and the queue.
def levelOrderBottom(self, root):
    if root == None:
        return []

    result = deque()
    queue = deque()
    queue.append(root)

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

        result.appendleft(level_list)

    return result
