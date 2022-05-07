#TC = O(log N) and SC = O(1)

def count_rotations(arr):
    start, end =0, len(arr)-1

    # Fnd the largets element in the list i.e. the last element of the pre rotated array.
    while start < end:
        mid = start + (end - start)//2

        if arr[mid] > arr[mid+1]:
            start = mid
            break

        if arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if start == len(arr)-1:
        return 0
    else:
        return start+1


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()