def quickSorter(arr, left, right):
    arrLen = len(arr)
    if left < right:
        pivot = right
        splitIndex = spliting(arr, pivot, left, right)
        quickSorter(arr, left, splitIndex-1)
        quickSorter(arr, splitIndex+1, right)
    return arr

def spliting(arr, pivot, left, right):
    pivotValue = arr[pivot]
    splitIndex = left

    for i in range(left, right):
        if arr[i] < pivotValue:
            swapper(arr, i, splitIndex)
            splitIndex += 1

    swapper(arr, right, splitIndex)
    return splitIndex


def swapper(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Select first and last index as 2nd and 3rd parameters
print(quickSorter(numbers,0,len(numbers)-1))
