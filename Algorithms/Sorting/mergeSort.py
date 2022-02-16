#Merge sort: This sorting algorithm splits the array and then ressembles it in
#a sorted order.

arr = [99,44,6,2,1,5,63,87,283,4,0]

def mergesort(arr):
    lenArr = len(arr)
    if lenArr == 1:
        return arr
    #split the array in half.
    left,right=[],[]
    print(lenArr/2)
    for i in range(lenArr):
        if i<=(lenArr/2):
            left.append(arr[i])
        else:
            right.append(arr[i])
    print(arr, left, right)
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    leftLen,rightLen=len(left),len(right)
    leftIndex,rightIndex=0,0
    combinedArray=[]
    while leftIndex<leftLen and rightIndex<rightLen:
        #Check if left less than right
        #   if true then append to array
        #else
        #   append right to array

        #return array

print(mergesort(arr))
