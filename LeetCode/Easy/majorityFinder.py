#Majority finder: find the majority element in a list that occurs more than
# length/2 times.

#Hash map solution with TC=O(n) abd SC=O(n)
def majorityElement(self, nums):
    result, countMap, maxCount = 0, dict(), 0
    for num in nums:
        countMap[num] = 1 + countMap.get(num, 0)
        if countMap[num] > maxCount:
            maxCount, result = countMap[num], num
    return result

#SC=O(1) solution using Boyer-Moore voting algorithm which returns the majority
#element given that a an element occures atleast lenght/2 times in the list.
def majorityElement(self, nums):
    result, count = 0, 0
    for num in nums:
        if count == 0:
            result = num
            count += 1
        elif result == num:
            count += 1
        else:
            count -= 1
    return result
