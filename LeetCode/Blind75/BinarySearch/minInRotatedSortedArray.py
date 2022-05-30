# [0,1,2,4,5,6,7]
# [4,5,6,7,0,1,2]
# [6,7,0,1,2,3,4]

# TC = O(logN) and SC = O(1)

class Solution:
    def findMin(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        min_num = arr[l]

        while l <= r:
            if arr[l] < arr[r]:
                min_num = min(min_num, arr[l])
                return min_num

            mid = (l + r) // 2
            min_num = min(min_num, arr[mid])
            if arr[mid] >= arr[r]:
                l = mid + 1
            else:
                r = mid - 1

        return min_num