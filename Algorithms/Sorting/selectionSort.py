#Selection sort with TC = O(n^2) and SC = O(1)

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    smallest=0
    for i in range(len(array)):
        for j in range(i, len(array)-1):
            if array[smallest]>array[j+1]:
                smallest = j+1
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
    return array

print(selectionSort(numbers))
