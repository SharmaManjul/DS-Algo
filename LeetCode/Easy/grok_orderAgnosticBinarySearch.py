#TC = O(log N) since we are reducing our search range by half in every step
#SC = O(1)

def search(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    # boolean value to check if list is ascending or descending.
    is_asc = nums[start] < nums[end]

    # no matter what happens the start will always be less than or equal to the end.
    while start <= end:
        # due to possibility of integer overflow in some languages we calculate middle like this since if start is already
        #max integer value then adding end to it will over flow
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        if is_asc:
            # if ascending we want to move either start or end to where the target will be closest to.
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1