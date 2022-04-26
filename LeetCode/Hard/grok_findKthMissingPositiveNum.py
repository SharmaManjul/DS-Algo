#Trick is to first cyclic sort without caring for anything outside 1 to n. Then start adding missing values in result
#and while doing this keep track of all ignored values since k might not be over till len(nums) so the ignored values might
#be those nums. Then add additional values outside len till len(reult) not less than k and make sure not to insert the ignored values.

#TC = O(N) + O(N) + O(K) => O(N+K) and O(K)
def find_first_k_missing_positive(nums, k):
    i = 0
    result= []
    ignored = {}
    while i < len(nums):
        j = nums[i] -1
        if nums[i] >= 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1

    print("sorted: ",nums)

    for i in range(len(nums)):
        if len(result) < k:
            if nums[i] != i+1:
                result.append(i+1)
                ignored[nums[i]] = True

    i=1
    while len(result) < k:
        candidate_num = i + len(nums)
        if candidate_num not in ignored:
            result.append(candidate_num)
        i+=1

    return result

def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))

main()