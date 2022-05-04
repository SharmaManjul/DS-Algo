#TC = O(N^2) and SC = O(N^2)

def subsets(self, nums):
    subsets = []
    subsets.append([])

    for cur_num in nums:
        subset_len = len(subsets)
        for i in range(subset_len):
            copy_set = list(subsets[i])
            copy_set.append(cur_num)
            subsets.append(copy_set)

    return subsets