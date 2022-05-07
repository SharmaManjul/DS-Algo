#TC = O(log N) and SC = O(1)
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        # this means that the since the mid is greater none of the other elements matter.
        if arr[mid] > arr[mid + 1]:
            end = mid
        # since the mid is not greater then the greatest exists after mid.
        else:
            start = mid + 1

    return start