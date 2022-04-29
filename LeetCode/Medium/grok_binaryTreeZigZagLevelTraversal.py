#TC = O(N) and SC = O(N)

def zigzagLevelOrder(self, root):
    if root == None:
        return root

    queue = deque()
    zigzag_tracker = 1
    queue.append(root)
    result = []

    while queue:
        level_len = len(queue)
        list_level = deque()

        for _ in range(level_len):
            # Using a counter to ensure we flip to zig zag.
            if zigzag_tracker % 2 == 0:
                cur_node = queue.popleft()
                list_level.appendleft(cur_node.val)
            else:
                cur_node = queue.popleft()
                list_level.append(cur_node.val)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        zigzag_tracker += 1

        result.append(list_level)

    return result