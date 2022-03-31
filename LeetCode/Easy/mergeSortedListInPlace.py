#Merge two descending sorted lists in place.

#With TC=O(n) and SC=O(1)
def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[(m + n) - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[(m + n) - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]