#TC = O(log N) and SC =O(1)

def searchRange(self, nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    if not nums:
        return result

    left_index = self.index_finder(nums, target, False)
    if nums[left_index] != -1:
        right_index = self.index_finder(nums, target, True)
        return [left_index, right_index]
    return result


def index_finder(self, nums, target, side):
    start, end = 0, len(nums) - 1
    key_index = -1
    while start <= end:
        mid = start + (end - start) // 2

        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            key_index = mid
            if side:
                start = mid + 1
            else:
                end = mid - 1

    return key_index