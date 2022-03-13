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

#Using two pointer method with sorting, TC=O(n logn) and SC = O(n)
def intersect(self, nums1, nums2):
    nums1.sort()
    nums2.sort()

    pt1, pt2, res = 0, 0, []

    while pt1 < len(nums1) and pt2 < len(nums2):
        if nums1[pt1] < nums2[pt2]:
            pt1 +=1
        elif nums1[pt1] > nums2[pt2]:
            pt2 +=1
        else:
            res.append(nums1[pt1])
            pt1 += 1
            pt2 += 1
    return res
