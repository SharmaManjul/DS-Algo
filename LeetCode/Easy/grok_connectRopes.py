# TC = O(N * logN) and SC = O(N)

def connectSticks(self, sticks: List[int]) -> int:
    # Edge case
    if not sticks:
        return 0

    # Put all sticks in min heap
    stick_heap = []
    for stick in sticks:
        heapq.heappush(stick_heap, stick)

    # Add sticks two at a time to make big stick.
    total_cost = 0
    while len(stick_heap) > 1:
        small_cost = heapq.heappop(stick_heap) + heapq.heappop(stick_heap)
        total_cost += small_cost
        heapq.heappush(stick_heap, small_cost)
    return total_cost