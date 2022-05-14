# # Using recursion and top down approach.
# # TC = O(2^N) and SC = O(N)
# def can_partition(nums):
#     return min_diff_finder(nums, 0, 0, 0)
#
#
# def min_diff_finder( nums, index, sum1, sum2):
#     if index == len(nums):
#         return abs(sum1 - sum2)
#
#     diff1 = min_diff_finder(nums, index + 1, sum1 + nums[index], sum2)
#     diff2 = min_diff_finder(nums, index + 1, sum1, sum2 + nums[index])
#
#     return min(diff1, diff2)
#
# def main():
#     print("Can partition: " +r(can_partition([1, 2, 3, 9])))
#     print("Can partition: " + st str(can_partition([1, 2, 7, 1, 5])))
#     print("Can partition: " + str(can_partition([1, 3, 100, 4])))
#
# main()



# Bottom up dynamic approach using tabular method. So the total sum of the list gives us the max possible sum, this sum
# in half gives the potential sum of two sets with difference 0. So what we need to find is if the sum exists for all the
# combinations of the sums and elements.
# If the last element of the dp array is False that means that the a set of sum = sum/2 doesn't exist so we need to look
# for a true value in the same index.

# TC = O(N * S) and SC = O(N * S)
def can_partition(nums):
    # Edge case
    if not nums:
        return None

    # This is the desiered sum for a subset to get us the min diff.
    full_sum = sum(nums)
    n_sum = full_sum // 2

    dp = [[x for x in range(0, n_sum+1)] for y in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for s in range(1, n_sum+1):
        if nums[0] == s:
            dp[0][s] = True
        else:
            dp[0][s] = False

    for i in range(1, len(nums)):
        for s in range(1, n_sum+1):
            is_valid1, is_valid2 = False, False

            if nums[i] <= s:
                is_valid1 = dp[i-1][s-nums[i]]

            is_valid2 = dp[i-1][s]

            dp[i][s] = is_valid2 or is_valid1

    for s in range(n_sum, -1, -1):
        if dp[len(nums)-1][s]:
            subset_sum1 = s
            subset_sum2 = full_sum - subset_sum1
            return abs(subset_sum1 - subset_sum2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

main()