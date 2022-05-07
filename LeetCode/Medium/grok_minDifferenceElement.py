#TC= O(logN) and SC= O(1)

def search_min_diff_element(arr, key):
    start, end = 0, len(arr)-1
    # if key is greater than last element of array then return last element.
    if key > arr[end]:
        return arr[end]

    while start <= end:
        mid = start + (end-start)//2
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return arr[mid]

    #After BS we will be left with start and end, since start is always mid+1 we subtract it with key and since end is
    #alwasy mid-1 we subtract key with end.
    if (arr[start] - key) < (arr[end] - key):
        return arr[start]
    return arr[end]

def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
