#O(N * logK) and SC = O(K)

def smallestRange(self, nums: List[List[int]]) -> List[int]:
    # Edge case
    if not nums:
        return []

    # Add first elements into heap
    min_heap = []
    range_start, range_end = 0, math.inf
    biggest_in_range = -math.inf
    for i in range(len(nums)):
        heapq.heappush(min_heap, [nums[i][0], 0, i])
        biggest_in_range = max(biggest_in_range, nums[i][0])

    # Loop until we cant have elements from each list.
    while len(min_heap) == len(nums):
        cur_small, cur_i, num_i = heapq.heappop(min_heap)  # Smallest element of the heap

        if range_end - range_start > biggest_in_range - cur_small:
            range_start = cur_small
            range_end = biggest_in_range

        if len(nums[num_i]) > cur_i + 1:
            heapq.heappush(min_heap, [nums[num_i][cur_i + 1], cur_i + 1, num_i])
            biggest_in_range = max(biggest_in_range, nums[num_i][cur_i + 1])

    return [range_start, range_end]
