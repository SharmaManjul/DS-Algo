#TC = O(logN) and SC = O(1)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_start, mountain_end = 0, mountain_arr.length() - 1

        # Finding the peak of the moutain.
        while mountain_start < mountain_end:
            mountain_mid = mountain_start + (mountain_end - mountain_start) // 2

            if mountain_arr.get(mountain_mid) > mountain_arr.get(mountain_mid + 1):
                mountain_end = mountain_mid
            else:
                mountain_start = mountain_mid + 1

        # Spliting mountain into two sorted list.
        acs_start = 0
        acs_end = desc_start = mountain_start
        desc_end = mountain_arr.length() - 1

        # Binary search in asceding part.
        asc_index = self.target_finder(acs_start, acs_end, mountain_arr, target, True)

        if asc_index != -1:
            return asc_index

        # Binary search in descending part.
        desc_index = self.target_finder(desc_start, desc_end, mountain_arr, target, False)

        return desc_index

    # Binary search for target. Ascending order is True and Descending is False
    def target_finder(self, start, end, arr, target, order):
        while start <= end:
            mid = start + (end - start) // 2

            if target > arr.get(mid):
                if order:
                    start = mid + 1
                else:
                    end = mid - 1
            elif target < arr.get(mid):
                if order:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                return mid

        return -1