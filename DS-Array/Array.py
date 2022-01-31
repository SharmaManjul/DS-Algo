array = ['aaa','b','cc','ddddd']

print(array[2])

#push
array.append('e')   # Adds one element to the end of array, O(1)

#pop
array.pop()    # Deletes one element from the end of array, O(1)

#addelement
array.insert(0,'z')    #Add element to specified index, O(n)


print(array)
