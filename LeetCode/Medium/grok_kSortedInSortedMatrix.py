# Using min heap and sorted nature of the matrix.
#TC = O(min(K, N) + N * logK) and SC = O(K)

def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    # Edge case
    if not matrix:
        return 0

    # Add first element of each row into heap.
    min_heap = []
    for i in range(min(k, len(matrix))):
        heapq.heappush(min_heap, [matrix[i][0], 0, i])

    cur, count = 0, 0
    while min_heap:
        cur, cur_i, list_i = heapq.heappop(min_heap)
        count += 1
        if count == k:
            break
        if len(matrix[list_i]) > cur_i + 1:
            heapq.heappush(min_heap, [matrix[list_i][cur_i + 1], cur_i + 1, list_i])

    return cur

