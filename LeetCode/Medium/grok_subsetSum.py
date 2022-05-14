# Bottom up using tabular: x axis of the table is the indexes and y axis is all the possible sums starting from 0.
# for every single element in nums we are going to check if a sum is possible either by including it or excluding it.

#TC = O(N * S) and SC = O(N * S)
def can_partition(nums, target_sum):
    # Edge case
    if not nums:
        return False

    dp = [[x for x in range(0, target_sum+1)] for y in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for s in range(1, target_sum+1):
        if nums[0] == s:
            dp[0][s] = True
        else:
            dp[0][s] = False

    for i in range(1, len(nums)):
        for s in range(1, target_sum+1):
            is_Valid1, is_valid2 = False, False

            if nums[i] <= target_sum:
                is_valid1 = dp[i-1][s-nums[i]]

            is_valid2 = dp[i-1][s]

            dp[i][s] = is_valid1 or is_valid2

    return dp[len(nums)-1][target_sum]

# Improved space complexity by only storing to lists ie a prev and cur.
# TC = O(N*S) and SC = O(2*S) = O(S)
def can_partition(nums, target_sum):
    # Edge case
    if not nums:
        return False

    dp = [[x for x in range(0, target_sum+1)] for y in range(2)]

    for i in range(2):
        dp[i][0] = True

    for s in range(1, target_sum+1):
        if nums[0] == s:
            dp[0][s] = True
        else:
            dp[0][s] = False

    for i in range(1, len(nums)):
        for s in range(1, target_sum+1):
            is_Valid1, is_valid2 = False, False

            if nums[i] <= target_sum:
                is_valid1 = dp[(i-1)%2][s-nums[i]]

            is_valid2 = dp[(i-1)%2][s]

            dp[i%2][s] = is_valid1 or is_valid2

    return dp[1][target_sum]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()