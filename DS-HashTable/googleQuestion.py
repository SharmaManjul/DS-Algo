# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
#
# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
#
# Given an array = [2,3,4,5]:
# It should return undefined
array = [2,1,1,2,3,5,1,2,4]
array1 = [2,3,4,5]
array2 = [2,5,5,2,3,5,1,2,4]
#Brute Force:
#Use two nested for loops, one to store the element and other to search the array.
#Scalability issues, time complexity is O(n^2)

#Hash Table: since it has easy lookup O(n).
#TC=O(n) and SC=O(n)
def firstRecuringCharacter(Array):
    arrayHashTable = dict()
    for item in Array:
        if item in arrayHashTable:
            return True
        else:
            arrayHashTable[item] = True
    return False


#print(firstRecuringCharacter(array1))



# Bonus... What if we had this:
#  [2,5,5,2,3,5,1,2,4]
#  return 5 because the pairs are before 2,2
def bonusFirstRecuringCharacter(Array):
    arrayHashTable = dict()
    for item in Array:
        if item in arrayHashTable:
            return item
        else:
            arrayHashTable[item] = True

print(bonusFirstRecuringCharacter(array2))
