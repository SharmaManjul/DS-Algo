# TC = O(N * logK) where N is all elements and K is the number of lists in input, SC = O(K)

import heapq

def find_Kth_smallest(lists, k):
    # Start by populating the min heap with the 1st element of all lists. Each node is an array of the element value,
    # element index and the list index.
    min_heap = []
    for i in range(len(lists)):
        heapq.heappush(min_heap, [lists[i][0], 0, i])

    # Loop till the heap is empty
    count_till_k = 0
    while min_heap:
        cur, cur_i, list_i = heapq.heappop(min_heap)
        count_till_k += 1
        if count_till_k == k:
            break
        if len(lists[list_i]) > cur_i+1:
            heapq.heappush(min_heap, [lists[list_i][cur_i+1], cur_i+1, list_i])

    return cur


def main():
    print("Kth smallest number is: " +
    str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))

main()
