#TC=O(N) and SC=O(N)
def insert(self, intervals, newInterval):
    res = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i][1] < newInterval[start]:
        res.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= newInterval[end]:
        newInterval[start] = min(newInterval[start], intervals[i][0])
        newInterval[end] = max(newInterval[end], intervals[i][1])
        i += 1

    res.append(newInterval)

    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res