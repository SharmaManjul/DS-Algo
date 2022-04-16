#Find unique triplets that equal to 0

#TC = O(N^2 + N * log(N)) which is O(N^2) and SC = O(N)
def threeSum(self, nums):
    # Sort the array O(N * log(N))
    nums.sort()
    triplet = []

    def triplet_finder(nums, target, left, triplet):
        right = len(nums) - 1

        #TC=O(N-1) or O(N)
        while left < right:
            #calculate current sum for every loop
            cur_sum = nums[left] + nums[right]

            #When we find triplet ensure no more duplicates from both the left and right side.
            if cur_sum == target:
                triplet.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif cur_sum > target:
                right -= 1
            else:
                left += 1

    # Given X look for Y+Z = -X, ensure X is not duplicate. TC=O(N)
    for first_index in range(len(nums) - 1):
        #Make sure you are not calling any duplicate Xs, if yes then skip
        if first_index > 0 and nums[first_index] == nums[first_index - 1]:
            continue
        #Call method with target as -X for Y+Z in range index of X+1 and range of nums.
        triplet_finder(nums, -nums[first_index], first_index + 1, triplet)

    return triplet