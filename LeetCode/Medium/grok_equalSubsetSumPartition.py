# # Top down approach using recurssion.
# # TC = O(2^N) and SC = O(N)
# def can_partition(num):
#     # First lets just calculate the total sum possinle of the list so that the two subsets will have their sum as the
#     # total sum / 2 and not we just need to look at all the possible combinations of subset and check if we have one that
#     #  equal to sum / 2. We only need to find one subset with sum equal to sum/2 since it is the half of the total sum so
#     # it is guarenteed that another subset with the same sum exists.
#
#     num_sum = 0
#     for n in num:
#         num_sum += n
#     # If the sum is odd then we can't find a patrition with its half since we need an even number for whole division.
#     if num_sum % 2:
#         return False
#     # The sum we want look for
#     partition_sum = num_sum//2
#
#     return partition_checker(num, partition_sum, 0)
#
# def partition_checker(num, partition_sum, index):
#     # Base checks
#     # Since this means that the required sum was successfully found.
#     if partition_sum == 0:
#         return True
#     n = len(num)
#     # If the empty list or the index has gone out of bound without partition sum equaling to 0.
#     if n == 0 or index >= n:
#         return False
#
#     # Lets make a recursive call for including the current element if it is less than the sum.
#     if num[index] <= partition_sum:
#         if(partition_checker(num, partition_sum-num[index], index+1)):
#             return True
#
#     # Call another recursive function if we don't include current element.
#     return partition_checker(num, partition_sum, index+1)
#
# def main():
#     print("Can partition: " + str(can_partition([1, 2, 3, 4])))
#     print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
#     print("Can partition: " + str(can_partition([2, 3, 4, 6])))
#
# main()



# Top down approach using recurssion with memoization.
# TC = O(N * S) and SC = O(N * S) where S is the total sum.
def can_partition(num):
    # First lets just calculate the total sum possinle of the list so that the two subsets will have their sum as the
    # total sum / 2 and not we just need to look at all the possible combinations of subset and check if we have one that
    #  equal to sum / 2. We only need to find one subset with sum equal to sum/2 since it is the half of the total sum so
    # it is guarenteed that another subset with the same sum exists.

    num_sum = 0
    for n in num:
        num_sum += n
    # If the sum is odd then we can't find a patrition with its half since we need an even number for whole division.
    if num_sum % 2:
        return False
    # The sum we want look for
    partition_sum = num_sum//2
    hash_map = {}

    return bool(partition_checker(hash_map, num, partition_sum, 0))

def partition_checker(hash_map, num, partition_sum, index):
    # Base checks
    # Since this means that the required sum was successfully found.
    if partition_sum == 0:
        return 1
    n = len(num)
    # If the empty list or the index has gone out of bound without partition sum equaling to 0.
    if n == 0 or index >= n:
        return 0

    # Lets make a recursive call for including the current element if it is less than the sum.
    if (index, partition_sum) not in  hash_map:
        if num[index] <= partition_sum:
            if (partition_checker(hash_map, num, partition_sum-num[index], index+1)) == 1:
                hash_map[(index, partition_sum)] = 1
                return 1

        # Call another recursive function if we don't include current element.
        hash_map[(index, partition_sum)] = partition_checker(hash_map, num, partition_sum, index+1)

    return hash_map[(index, partition_sum)]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))

main()
