#TC = O(N) and SC = O(N)

def averageOfLevels(self, root):
    if root == None:
        return root

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_sum = 0.0
        level_len = len(queue)

        for _ in range(level_len):
            cur_node = queue.popleft()
            level_sum += cur_node.val

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        result.append(level_sum / level_len)

    return result