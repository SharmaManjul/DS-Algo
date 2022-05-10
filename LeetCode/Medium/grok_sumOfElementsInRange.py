# TC = O(N * logK2) and SC = O(K2)

import heapq

def find_sum_of_elements(nums, k1, k2):
    # Edge case
    if not nums or k1 < 0 or k2 < 0 or k1 > len(nums) or k2 > len(nums):
        return 0
    if k1 == k2:
        return nums[k1]

    # Loop thorugh list and add k2 elements to a max_heap.
    # TC = O(N * logK2)
    max_heap = []
    for i in range(len(nums)):
        if i < k2-1:
            heapq.heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -nums[i])

    # Loop through the max heap while popping it k2 - k1 -1 times, since the top node in the max heap will be the k2-1th
    # element so we only neeed to loop k2 - k1 -1 time to add up till the k1th element.
    sum = 0
    for _ in range(k2 - k1 - 1):
        sum += -heapq.heappop(max_heap)

    return sum


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
    str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
    str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))

main()