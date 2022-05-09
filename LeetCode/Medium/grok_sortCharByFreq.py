# TC = O(N * logN) and SC = O(N)

def frequencySort(self, s: str) -> str:
    # Edge case
    if not s:
        return ""

    # Create freuency map
    s_map = {}
    for i in s:
        if i in s_map:
            s_map[i] += 1
        else:
            s_map[i] = 1

    # Populate the max heap
    max_heap = []
    for i in s:
        heapq.heappush(max_heap, (-s_map[i], i))

    # Extract string chracter from the max heap and join as a string.
    result = []
    for i in s:
        result.append(heapq.heappop(max_heap)[1])

    return "".join(result)