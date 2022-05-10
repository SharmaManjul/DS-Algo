# TC = O(logN + K * LogK) and SC = O(k)

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # Edge case
    if not arr:
        return []

    # Binary search to find X or the closest number to X in arr
    x_index = self.binary_search(arr, x)

    # Add all elements from k-x_index to k+x_index into a min heap.
    min_heap = []
    # Edge case: if kis outside len bounds.
    x_start = max(x_index - k, 0)
    x_end = min(x_index + k, len(arr) - 1)
    #O(2K * log2K)
    for i in range(x_start, x_end + 1):
        heapq.heappush(min_heap, (abs(arr[i] - x), arr[i]))

    # Pop heap and add result to list.
    result = []
    for _ in range(k):
        result.append(heapq.heappop(min_heap)[1])

    result.sort()
    return result

# O(logN)
def binary_search(self, arr, x):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    if start == 0:
        return start
    return start - 1