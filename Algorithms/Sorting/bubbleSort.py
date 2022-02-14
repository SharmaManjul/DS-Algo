#Bubble sort with TC = O(n^2) and SC = O(1)

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def swapper(left, right):
    temp = array[right]
    array[right] = array[left]
    array[left] = temp

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubbleSort(numbers))
