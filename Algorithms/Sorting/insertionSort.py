#Insertion sort with TC = O(n^2) and SC = O(1)
#When list nearly sorted the TC is O(n)

numbers = [99, 44, 6, 2, 1, 5, 87, 63, 283, 4, 0]

def insertionSort(array):
    lenArray = len(array)
    i=1
    last=array[0]
    while i<lenArray:
        if array[i]<last:
            itemStore = array.pop(i)
            for j in range(0,i):
                if itemStore<array[j]:
                    array.insert(j,itemStore)
                    break
        last=array[i]
        i+=1
    return array

print(insertionSort(numbers))
