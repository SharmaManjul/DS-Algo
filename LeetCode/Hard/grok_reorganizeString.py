# TC = O(N * logN) and SC = O(N)

def reorganizeString(self, s: str) -> str:
    # Add to frequency map
    string_map = {}
    for i in s:
        if i in string_map:
            string_map[i] += 1
        else:
            string_map[i] = 1

    # Add all characters to heap
    max_heap = []
    for string in string_map:
        heapq.heappush(max_heap, (-string_map[string], string))

    # Alternate among heap elements based on their frequencies. The trick is to maintain a a prev count and char, which
    # once popped can only be added back if it's count is more than 0 and it is not None. This allows us to alternate the
    # heap with valid characters and add them to the result list. If a string's characters can't be combined in the required
    # way the returned result will be less than the length of the input as the input would fail to meet algo requirements,
    # in that case we return empty string.
    result = []
    prev_count, prev = 0, None
    while max_heap:
        cur_count, cur = heapq.heappop(max_heap)

        if -prev_count > 0 and prev:
            heapq.heappush(max_heap, (prev_count, prev))

        result.append(cur)
        prev_count, prev = cur_count + 1, cur

    return "".join(result) if len(result) == len(s) else ""