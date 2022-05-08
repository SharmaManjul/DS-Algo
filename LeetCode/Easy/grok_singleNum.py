# TC = O(N) and SC = O(1)

def singleNumber(self, nums: List[int]) -> int:
    missing_num = 0

    for num in nums:
        missing_num = missing_num ^ num

    return missing_num
