# The main trick for this question is that once/when we know the biggest end time we just need to keep checking all the
# starts against it and since the starts are sorted we dont have to worry about missing any free time in the front. So that
# is why we care to find the max end time.

# TC = O(N * logN) and SC = O(N)

def employeeFreeTime(self, schedule):

    # Error checking
    if not scheudle:
        return []

    # Appending all intervals to a list sorted by start time.
    all_schedules = []
    for times in schedule:
        for time in times:
            all_schedules.append(time)
    all_schedules.sort(key=lambda x: x.start)

    # Find free intervals by keep track of max end time.
    free_time = []
    end_time = all_schedules[0].end
    for i in range(1, len(all_schedules)):
        start_time = all_schedules[i].start
        cur_end_time = all_schedules[i].end
        if start_time > end_time:
            free_time.append(Interval(end_time, start_time))
        end_time = max(end_time, cur_end_time)

    return free_time


# In the solution above we don't take advantage of the fact that each employees interval are sorted indivudually.

# TC = O(N * logK) where N is the number of intervals and K is the number of employees. The TC is because we will loop
# every interval and for each interval we will push and pop from the heap which at most will only have elements the number
# of employees.
    def employeeFreeTime(self, schedule):
        # Error checking
        if not schedule:
            return []

        # creating the min heap with the first elements of each employee.
        results = []
        min_heap = []

        # Pushing (interval.start, employee index, interval index) to the min heap, so heap is sorted by start times.
        for i in range(len(schedule)):
            heapq.heappush(min_heap, (schedule[i][0].start, i, 0))

        # Find the free time for all employees.
        # Get the first element of the heap and get the end associated to the interval
        _, employee_index, interval_index = min_heap[0]
        prev_end = schedule[employee_index][interval_index].end
        while min_heap:
            # Pop the smallest interval in the heap.
            _, cur_employee_index, cur_interval_index = heapq.heappop(min_heap)

            # Push next interval of the smal employee to the list.
            if cur_interval_index + 1 < len(schedule[cur_employee_index]):
                heapq.heappush(min_heap, (
                schedule[cur_employee_index][cur_interval_index + 1].start, cur_employee_index, cur_interval_index + 1))

            # Grab the current interval/event to compare if the start of the cur is greater than the end of the prev. If so
            # add initialized object to results.
            cur_event = schedule[cur_employee_index][cur_interval_index]
            if cur_event.start > prev_end:
                results.append(Interval(prev_end, cur_event.start))
            # Update prev_end to the max between itself and the cur_event.
            prev_end = max(prev_end, cur_event.end)

        return results