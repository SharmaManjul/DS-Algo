# TC = O(N logN + K logN) and SC = O(N)

import heapq

def find_maximum_distinct_elements(nums, k):
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

    # Store nums with frequencies 2 or more in a min heap.
    # TC = O(N logN) and SC = O(N)
    distinct_count = 0
    min_heap = []
    for num in num_map:
        if num_map[num] > 1:
            heapq.heappush(min_heap, (num_map[num], num))
        else:
            distinct_count += 1

    # Pop min heap nodes can reduce k by freq-1 until k not more than 0 or min_heap empty
    # TC = O(K logN) and SC = O(1)
    while k > 0 and min_heap:
        num_freq, _ = heapq.heappop(min_heap)
        k -= num_freq-1
        if k >= 0:
            distinct_count += 1

    #Check if anymore k is left, happens when everything is distinct and k is still remaining. So reduce distinct count.
    if k > 0:
        distinct_count -= k

    return distinct_count

def main():
    print("Maximum distinct numbers after removing K numbers: " +
    str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
    str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
    str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],2)))

main()