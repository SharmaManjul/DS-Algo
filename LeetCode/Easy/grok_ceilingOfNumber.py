#TC = O(log N) and SC = O(1)

def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr)-1
    # check if given key is greater than the greatest element in list and return -1
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        # Binary search for key in list and return the index if key found in list.
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return mid

    # once binary search is completed then that means that the end is less than start which in turn means that start is
    # at the closest element where the element is greater than key.
    return start



def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
