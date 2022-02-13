#TODO: Collection of numbers, find a matching pair that is equal to the sum given to us.

#Examples:
#[1,2,3,9] sum=8
#[1,2,4,4] sum=8

#Notes:
#Integers and -ves can happen.
#Ascending order and an array
#Output: true or false
#no repeat
#infinte

#Naive Approach:
#Time complexity, nestes loops > O(n^2), not scalable.

array1 = [1,2,4,5,9]
array2 = [1,2,3,4,6]
sum = 8

def integerMatcher(array, sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j) and (sum == (array[i] + array[j])):
                    return True
    return False

# print(integerMatcher(array2, sum))

#Ordered, pairs!

def betterIntegerMatcher(array, desiredSum):
    high = len(array)-1
    low = 0
    print(low, high)
    while low < high:
      pairSum = array[low] + array[high]
      print("pair",pairSum)
      if pairSum == desiredSum:
        return True
      elif pairSum < desiredSum:
        low += 1
        print("low", low)
      else:
        high -= 1
        print("high", high)
    return False


# print("test")
# print(betterIntegerMatcher(array1, sum))

#What if the arrays were unordered?
#We need some datastructure to store the items which allows us to chekc is the complement exists
#hashmaps or dictionary is a good candidate fo this, we can check if complement exists and if not add items in the dict and keep going until we find something or not.

def bestIntegerMatcher(array, desiredSum):
  hashMap = dict()
  for item in array:
    comp = desiredSum - item
    if not comp in hashMap:
      hashMap[item] = True
    else:
      return True
  return False

print(bestIntegerMatcher(array1, sum))
