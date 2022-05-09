# TC = O(N + N * logK) and SC = O(N)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Edge case
    if not nums or k == 0:
        return []

    # Creating frequency map
    # TC = O(N) and SC = O(N)
    num_freq = {}
    for num in nums:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    # Add k elements to min heap and keep removing min element and adding new elements until k. Use
    # tuple data structure in heap tp keep track of num and its frequency.
    # TC = O(N * logK) and SC = O(K)
    min_heap = []
    for num in num_freq:
        heapq.heappush(min_heap, (num_freq[num], num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Pop out the heap till it's empty and store the result in a list.
    # TC = O(logK) and SC = O(1)
    top_freq = []
    while min_heap:
        top_freq.append(heapq.heappop(min_heap)[1])

    return top_freq