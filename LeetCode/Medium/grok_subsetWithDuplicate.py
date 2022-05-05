#TC = O(N^2) and SC = O(N^2)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Sort the list so all the suplicates are together.
        nums.sort()
        subsets = []
        subsets.append([])
        start, end = 0, 0

        for i in range(len(nums)):
            start = 0
            #Check is duplicate found and set start of subset to end which is currently the end of prev.
            if i > 0 and nums[i] == nums[i - 1]:
                start = end
            end = len(subsets)
            #Normally create subsets within the bounds of start and end.
            for j in range(start, end):
                set = list(subsets[j])
                set.append(nums[i])
                subsets.append(set)

        return subsets