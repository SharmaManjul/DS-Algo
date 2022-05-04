#TC = O(N * K) and SC = O(K)

class Solution:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        results = []

        for i in range(len(nums)):
            # Add every element of nums into the max heap
            heapq.heappush(self.max_heap, -nums[i])

            # Make sure that every element inside max heap is <= min heap.
            if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
                val = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -val)

            # Reorganize heap
            self.reorg_heap()

            # Check if we have window of len k
            if i - k + 1 >= 0:
                # Find the median using two heap
                if len(self.max_heap) > len(self.min_heap):
                    results.append(float(-self.max_heap[0]))
                if len(self.min_heap) > len(self.max_heap):
                    results.append(float(self.min_heap[0]))
                if len(self.max_heap) == len(self.min_heap):
                    results.append(float((-self.max_heap[0] + self.min_heap[0]) / 2))

                # Remove first element of window from heap, the i-k+1th element.
                num_to_remove = nums[i - k + 1]
                # Check in which heap is the num
                if num_to_remove <= -self.max_heap[0]:
                    self.remove_node(self.max_heap, -num_to_remove)
                else:
                    self.remove_node(self.min_heap, num_to_remove)

                # Reorganize heap
                self.reorg_heap()

        # Return result
        return results

    def reorg_heap(self):  # O(logN)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def remove_node(self, heap, num):
        i = heap.index(num)  # O(logN)
        heap[i] = heap[-1]
        del heap[-1]
        heapq.heapify(heap)  # O(N) Not good

        if i < len(heap):  # O(log N) Better
            heapq._siftup(heap, i)
            heapq._siftdown(heap, 0, i)