#TC = O(log N) and SC=O(N)

class MedianFinder:

    def __init__(self):
        # Two heaps: small => maxheap so that it store the smallest element and the oth node is the largest,
        # large => minheap so that it stores the biggest elements and the oth node is the smallest.
        #These heaps let us always know what the median is since the Oth element of each heaps is readily available.
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Python defaults to a min heap so to ensure small is a max heap we will multiply every element by -1.
        heapq.heappush(self.small, -num)

        # We want every element in small to be <= large. So that we can sort the data stream since the small heap will
        #be sorted on its own and the same with the large heap, this means that is small <= large the entire data stream
        #is sorted.
        # when the max element of small is > the max element of large, we want to move the max element of small to large.
        #We need to do this to ensure that the data is sorted.
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = heapq.heappop(self.small)  # O(logN)
            heapq.heappush(self.large, -val)  # O(logN)

        # We dont want the heap to be uneven in length i.e. a difference of more than 1. If so then reorganize the heaps.
        # An uneven len means that the oth node of each heap is not pointing to the actual median.
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)  # O(logN)
            heapq.heappush(self.large, -val)  # O(logN)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)  # O(logN)
            heapq.heappush(self.small, -val)  # O(logN)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]  # O(1)
        if len(self.large) > len(self.small):
            return self.large[0]  # O(1)

        return (-self.small[0] + self.large[0]) / 2
