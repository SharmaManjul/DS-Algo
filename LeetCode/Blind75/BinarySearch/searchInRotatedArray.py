# Since the list is rotated we can imagine it as two separate lists on which we want to run binary search. If the target
# is smaller than the smallest num in left list then it might exist on the right side of mid. If the target is greater
# than the rightmost num in the second right list, then it might exist in the left list so right is to the left of mid.

# TC = O(logN) and SC = O(1)

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            if arr[l] <= arr[mid]:
                if target > arr[mid] or target < arr[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < arr[mid] or target > arr[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1