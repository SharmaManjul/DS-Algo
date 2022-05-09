# TC for add() is O(logK) and SC = O(K)

class KthLargest:
    # Class variable min heap to store all the biggest k elements
    min_heap = []

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for num in nums:
            self.add(num)

    # Method responsible for adding to the heap and maintaining top k elements.
    # O(log K)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]