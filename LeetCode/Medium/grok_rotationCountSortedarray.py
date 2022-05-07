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

# More readable solution:
def findMin(self, arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    # Fnd the largets element in the list i.e. the last element of the pre rotated array.
    while start < end:
        mid = start + (end - start) // 2
        # Check if mid within bounds to prevent calculating mid+1 or mid-1 and if all good return minimum
        if mid < end and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        if mid > start and arr[mid] < arr[mid - 1]:
            return arr[mid]

        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    # If not returns in the while that means list is not rotated.
    return arr[0]


# Rotation with duplication.

    def findMin(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start < end:
            mid = start + (end - start) // 2

            # Check if mid within bounds to prevent calculating mid+1 or mid-1 and if all good return minimum
            if mid < end and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]
            if mid > start and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # If start, mid and end are equal we need to shrink the window size but also check for any condition violations.
            if arr[start] == arr[mid] and arr[end] == arr[mid]:
                if arr[start] > arr[start + 1]:
                    return arr[start + 1]
                start += 1

                if arr[end] < arr[end - 1]:
                    return arr[end]
                end -= 1

            elif arr[start] <= arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return arr[0]