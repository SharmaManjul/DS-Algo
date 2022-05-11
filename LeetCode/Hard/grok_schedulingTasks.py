# TC = O(N * log26) => O(N) and SC = O(N)

def leastInterval(self, tasks: List[str], n: int) -> int:
    # Edge case
    if not tasks or n < 0:
        return 0

    # Create freq map using counter and the max heap
    task_map = Counter(tasks)
    max_heap = [-x for x in task_map.values()]
    # Heapifuy the list to create a max heap.
    heapq.heapify(max_heap)
    queue = deque()  # [count of task, time when task can be processed]

    # While either the heap or q has elements inside we want to keep looping and increament time. Inside while heap
    # we want to pop the heap and is the count is more than zero we want to decreament it and add it to the queue with
    # the expected time at which this task can be processed again (time + n). Then if queue and the time of its first
    # element is equal to the current time we want to we want to pop the queue and append to the heap.

    # TC = O(N * log26)
    time = 0
    while max_heap or queue:
        time += 1
        if max_heap:
            count = 1 + heapq.heappop(max_heap)
            if count:
                queue.append([count, time + n])
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])

    return time