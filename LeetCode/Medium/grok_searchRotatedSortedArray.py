# TC = O(logN) and worst case of duplicates O(N) and SC=(1)

def search_rotated_array(arr, key):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == key:
            return mid

        # shrinking window to account for duplicates
        # if entire list is duplicate and key is not the duplicate then we will end up looping N/2 times making the worst
        # case be O(N)
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1
        # ascending order from start to mid so if key exists inside adjust end or adjust start.
        elif arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # ascending order from mid to end so if key exists inside adjust start else adjust end.
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([3, 7, 3, 3, 3], 7))

main()
