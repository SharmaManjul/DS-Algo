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

#Follow up questions:
    #Q: What if the given array is already sorted? How would you optimize your algorithm?
    #A: If already sorted then no need to perform sortion and TC wil be O(n)

    #Q: What if nums1's size is small compared to nums2's size? Which algorithm is better?
    #A: We should use the hash map solution because a smaller hashmap will be faster and have less collisions

    #What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    #A: Build hash map with nums1 and process nums2 in chunks that fit in memory.
