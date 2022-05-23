# Used a hash map to store complements of the curnum with the target. As I was looping kept checking if list num existed in the map.
# TC = O(N) and SC = O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False