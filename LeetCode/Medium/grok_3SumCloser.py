#Find closest triplet to target.

#Trick is to use one pointer to loop the arr and the other two as left and right. Keep comparing until smallest difference is found.

#TC = O(N^2 + N logN) =>O(N^2) and SC = O(N)
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    initial_sum = arr[0] + arr[1] + arr[len(arr) - 1]
    for i in range(len(arr)):
        left = i+1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum - target_sum == 0:
                return 0
            elif current_sum > target_sum:
                right -= 1
            else:
                left += 1

            if abs(current_sum - target_sum) < abs(initial_sum - target_sum):
                initial_sum = current_sum

    return initial_sum


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()