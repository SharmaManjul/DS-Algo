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
