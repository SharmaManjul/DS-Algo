#TC = O(logN + logN) => O(logN) ans SC = O(1)

def search(self, reader: 'ArrayReader', target: int) -> int:
    start, end = 0, 1
    # O(log N)
    while reader.get(end) < target:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start
    return self.target_finder(start, end, reader, target)

def target_finder(self, start, end, reader, target):
    # O(log N)
    while start <= end:
        mid = start + (end - start) // 2
        if target > reader.get(mid):
            start = mid + 1
        elif target < reader.get(mid):
            end = mid - 1
        else:
            return mid
    return -1