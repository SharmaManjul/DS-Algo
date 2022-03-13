#Retrun the intersection of two arrays.

#Using hash map and an extra list to store result with TC=O(n) and SC=O(n)
def intersect(self, nums1, nums2):
    arrayMap = dict()
    for i in nums1:
        if i in arrayMap:
            arrayMap[i] += 1
        else:
            arrayMap[i] = 1
    res = []
    for j in nums2:
        if j in arrayMap and arrayMap[j]>0:
            res.append(j)
            arrayMap[j] -= 1
    return res
