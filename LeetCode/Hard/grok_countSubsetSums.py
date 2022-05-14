# # Recursively, TC = O(2^N) and SC = O(N)
# # With memoization TC = O(N * S) and SC = O(N * S)
# def count_subsets(num, sum):
#     dp = [[-1 for x in range(sum+1)] for i in range(len(num))]
#     return count_subsets_recursive(dp, num, sum, 0)
#
# def count_subsets_recursive(dp, num, sum, i):
#     if sum == 0:
#         return 1
#     if i == len(num):
#         return 0
#
#     if dp[i][sum] == -1:
#         sum1, sum2 =0, 0
#         if num[i] <= sum:
#             sum1 = count_subsets_recursive(dp, num, sum-num[i], i+1)
#         sum2 = count_subsets_recursive(dp, num, sum, i+1)
#
#         dp[i][sum] = sum1 + sum2
#
#     return dp[i][sum]
#
# def main():
#     print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
#     print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
#
# main()

def count_subsets(num, sum):
    n = len(num)
    dp = [[-1 for x in range(sum+1)] for y in range(2)]
    # populate the sum = 0 columns, as we will always have an empty set for zero sum
    for i in range(0, 2):
        dp[i][0] = 1
    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, sum+1):
        dp[0][s] = 1 if num[0] == s else 0
    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, sum+1):
            # exclude the number
            dp[i%2][s] = dp[(i - 1)%2][s]
            # include the number, if it does not exceed the sum
            if s >= num[i]:
                dp[i%2][s] += dp[(i - 1)%2][s - num[i]]
    # the bottom-right corner will have our answer.
    return dp[(n-1)%2][sum]

def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))

main()