#TC = O(N) and SC = O(Ng)
def minDepth(self, root):
    if root == None:
        return 0

    queue = deque()
    queue.append(root)
    level = 0

    while queue:
        level += 1

        for _ in range(len(queue)):
            cur_node = queue.popleft()

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

            if cur_node.left == None and cur_node.right == None:
                return level