#TC = O(N logN) and SC = O(N)

def findRightInterval(self, intervals):
    start_heap, end_heap = [], []
    results = [-1 for i in range(len(intervals))]

    #Two max heaps to store the start and end of the intervals along with their index.
    #O(N logN)
    for i in range(len(intervals)):
        heapq.heappush(start_heap, (-intervals[i][0], i))
        heapq.heappush(end_heap, (-intervals[i][1], i))

    #Loop for each interval in intervals
    for _ in intervals:
        #Pop the max in heap of end intervals.
        cur_num, cur_index = heapq.heappop(end_heap)

        #Check if the max in start heap is greater or equal to max of end.
        if start_heap and -start_heap[0][0] >= -cur_num:
            next_num, next_index = heapq.heappop(start_heap)
            #Keep looping until you find the closest start to end.
            while start_heap and -start_heap[0][0] >= -cur_num:
                next_num, next_index = heapq.heappop(start_heap)

            #Add to results.
            results[cur_index] = next_index

            #Push the start element that was popped last which was closest to the end, this means that there is a chance
            #that this start could be the closest to the next max.
            heapq.heappush(start_heap, (next_num, next_index))

    return results
