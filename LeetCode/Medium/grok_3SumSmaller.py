#Find closest triplet to target.


#TC = O(N^2 + N logN) =>O(N^2) and SC = O(N)
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    counter = 0
    for i in range(len(arr)):
        left = i+1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum < target_sum:
                counter += 1
                right -= 1
            else:
                break

    return counter


def main():
    print(triplet_sum_close_to_target([-1, 0, 2, 3], 3))
    print(triplet_sum_close_to_target([-1, 4, 2, 1, 3], 5))



main()
