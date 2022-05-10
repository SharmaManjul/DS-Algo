# TC = O(N * logN) and SC = O(N + K)

def rearrangeString(self, s: str, k: int) -> str:
    # Edge case
    if not s or k > len(s) or k < 0:
        return []
    if k == 0:
        return s

    # Create frequency map.
    s_map = {}
    for char in s:
        if char in s_map:
            s_map[char] += 1
        else:
            s_map[char] = 1

    # Populate our max heap with all the frequencies and it's characters.
    max_heap = []
    for char in s_map:
        heapq.heappush(max_heap, (-s_map[char], char))

    # Loop thorugh all nodes of the heap and keep track of prev nodes processed
    # in a queue (FIFO) until len of the queue is k, then start adding queue characters
    # into result.
    result = []
    queue = deque()

    while max_heap:
        cur_count, cur = heapq.heappop(max_heap)
        queue.append((cur_count + 1, cur))

        if len(queue) == k:
            q_count, q = queue.popleft()
            if -q_count > 0:
                heapq.heappush(max_heap, (q_count, q))

        result.append(cur)

    return "".join(result) if len(result) == len(s) else ""