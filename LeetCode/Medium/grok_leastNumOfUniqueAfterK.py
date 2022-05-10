# TC = O(N * logN) and SC = O(N)

def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
    # Edge case
    if not nums:
        return []
    if len(nums) < k:
        return 0

    # Creating frequency map for nums.
    # TC = O(N) and SC = O(N)
    num_map = {}
    for num in nums:
        if num in num_map:
            num_map[num] += 1
        else:
            num_map[num] = 1

    distinct_count = len(num_map)
    min_heap = []
    for num in num_map:
        heapq.heappush(min_heap, (num_map[num], num))

    while k > 0 and min_heap:
        num_freq, _ = heapq.heappop(min_heap)
        k -= num_freq
        if k >= 0:
            distinct_count -= 1

    return distinct_count