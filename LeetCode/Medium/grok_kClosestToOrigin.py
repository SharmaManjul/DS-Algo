# TC = O(K * logK + K * logK + (N-K) * logK) => O(N * logK)
# SC = O(K)

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    max_heap = []

    # Find distance of K points to the origin and add to max heap.
    # O(K * logK)
    for i in range(k):
        distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        heapq.heappush(max_heap, (-distance, points[i]))

    # Find distance of all points after K and max heap if less than the max value.
    # O((N-K) * logK)
    for i in range(k, len(points)):
        distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)

        if -distance > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-distance, points[i]))

    # O(K * logK)
    for i in range(k):
        result.append(heapq.heappop(max_heap)[1])

    return result