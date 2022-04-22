#The trick here is to first sort the list by first elements and then since we know that the first elements are sorted,
#we only need to check for the second elements of the list. While condition to expand the interval is true (a.end >= b.stasrt)
#keep extending the end of the custom interval and else add to result and adjust custom interval. Finally the last list
#will not be added so go ahead and add that to the result.

#TC=O(N log N) and SC= O(N)
def merge(self, intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])
    res = []

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            end = max(end, intervals[i][1])
        else:
            res.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]

    res.append([start, end])

    return res