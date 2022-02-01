#Given two sorted arrays merge them into one sorted array.
#Are the arrays sorted in ascending order? yes, output is also ascending
#Can array have the same element? Yes
#Are these numbers integers? Yes
#main goal: time or space complexity? just make it efficient
#Brute force approach:
# for i in array1:
#   for j in array2:
#       if i<j and not mergeArray[i]:
#           add i to mergeArray
#       elif i>j and not mergeArray[i]:
#           add j to mergeArray


array1 = [1, 2, 4, 5, 7, 9, 10]
array2 = [3, 6, 9, 12, 13]
mergeArray= []
length1 = len(array1)
length2 = len(array2)

#Problem with this solution is that the time complexity is 0(a*b) where a and b
#are the length of the arrays. This doesn't offer scalabilty as the length increases.
def badMergeSorted(array1, array2, mergeArray):
    length1 = len(array1)
    length2 = len(array2)

    for i in range(length1):
        for j in range(length2):
            if (array1[i] < array2[j]) and (not array1[i] in mergeArray):
                mergeArray.append(array1[i])
                if (i+j) == (length1+length2-2):
                    mergeArray.append(array2[j])
            elif (array1[i] > array2[j]) and (not array2[j] in mergeArray):
                mergeArray.append(array2[j])
                if (i+j) == (length1+length2-2):
                    mergeArray.append(array1[i])

    print(mergeArray)

def badInputChecker(array1, array2):
    if (type(array1) is not list) and (type(array2) is not list):
        return "Type is not array."
    #check if all elements are integers
    if (len(array1) == 0) and (len(array2) == 0):
        print("Empty arrays")
        return True
    elif (len(array1) == 0):
        print(array2)
        return True
    elif (len(array2) == 0):
        print(array1)
        return True

#Better solution
#array1 = [1, 2, 4, 5*]
#array2 = [3, 6*, 9]
#Ooutput - [1, 2, 3, 4, 5]
def betterMergeSorted(array1, array2):
    if badInputChecker(array1, array2):
        return "Merge end"

    mergeArray= []
    i = 0
    j = 0

    if len(array1)==0 or len(array2)==0:
        return array1+array2

    while i<len(array1) and j<len(array2):
        if array1[i] < array2[j]:
            mergeArray.append(array1[i])
            i+=1
        elif array2[j] < array1[i]:
            mergeArray.append(array2[j])
            j+=1
        else:
            mergeArray.append(array2[j])
            mergeArray.append(array1[i])
            i+=1
            j+=1

    return mergeArray+array1[i:]+array2[j:]

print(betterMergeSorted(array1, array2))
