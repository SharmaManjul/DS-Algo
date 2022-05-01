#TC = o(N) and SC = O(N)

def rightSideView(self, root):
    if root == None:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_len = len(queue)
        for i in range(level_len):
            cur_node = queue.popleft()
            if i == level_len - 1:
                result.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return result