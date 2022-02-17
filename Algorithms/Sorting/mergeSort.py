#Merge sort: This sorting algorithm splits the array and then ressembles it in
#a sorted order.

arr = [99,44,6,2,1,5,63,87,283,4,0]

def mergesort(arr):
    lenArr = len(arr)
    if lenArr == 1:
        return arr
    #split the array in half.
    half=lenArr//2
    left=arr[:half]
    right=arr[half:]
    print('Left {}'.format(left))
    print('Right {}'.format(right))
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    leftIndex = 0
    rightIndex = 0
    combinedArray=[]
    while leftIndex<len(left) and rightIndex<len(right):
        print("left", left[leftIndex], "right", right[rightIndex])
        if left[leftIndex] < right[rightIndex]:
            combinedArray.append(left[leftIndex])
            leftIndex += 1
        else:
            combinedArray.append(right[rightIndex])
            rightIndex += 1

    print(left,right)
    print(combinedArray+left[leftIndex:]+right[rightIndex:])
    return combinedArray+left[leftIndex:]+right[rightIndex:]

print(mergesort(arr))
