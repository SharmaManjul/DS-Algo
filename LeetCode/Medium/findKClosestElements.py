#TC= O(logN + K) and SC= O(1)

# Here the idea is to use binary search to locate the element or find the element closest to x and the use sliding
# window to find the sub list.
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # using binary search to find the element of the closest element and use sliding window to locate all the closest elements till k.
    start, end = 0, len(arr) - 1
    #Value and index of x or an element close to x.
    value, index = arr[0], 0

    while start <= end:
        mid = start + (end - start) // 2

        # find the diff for mid and x and the prev value
        cur_diff, res_diff = abs(arr[mid] - x), abs(value - x)
        # if the cur diff is less than res diff or if they are equal and the value of mid is less than value update the
        # value and index.
        if cur_diff < res_diff or (cur_diff == res_diff and arr[mid] < value):
            value, index = arr[mid], mid

        if x > arr[mid]:
            start = mid + 1
        elif x < arr[mid]:
            end = mid - 1
        else:
            break

    left = right = index
    for i in range(k - 1):
        if left == 0:
            right += 1
        elif right == len(arr) - 1 or x - arr[left - 1] <= arr[right + 1] - x:
            left -= 1
        else:
            right += 1

    return arr[left:right + 1]

