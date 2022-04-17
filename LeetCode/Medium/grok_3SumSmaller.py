#Find all triplets smaller than target.


def triplet_finder(arr, left, target):
    count = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count

def triplet_lister(arr, i, target, res):
    left = i+1
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] < target:
            for j in range(right, left, -1):
                res.append([arr[i], arr[left], arr[j]])
            left += 1
        else:
            right -= 1


#TC = O(N^2 + N logN) =>O(N^2) and SC = O(N)
def triplet_sum_smaller_than_target(arr, target_sum):
    arr.sort()
    counter = 0
    res = []
    for i in range(len(arr) - 2):
        counter += triplet_finder(arr, i+1, target_sum - arr[i])
        triplet_lister(arr, i, target_sum - arr[i], res)
    return counter


#TC = O(N^2 + N logN) =>O(N^2) and SC = O(N)
def triplet_sum_list_smaller_than_target(arr, target_sum):
    arr.sort()
    res = []
    for i in range(len(arr) - 2):
        triplet_lister(arr, i, target_sum - arr[i], res)
    return res


def main():
    print(triplet_sum_smaller_than_target([-1, 0, 2, 3], 3))
    print(triplet_sum_smaller_than_target([-1, 4, 2, 1, 3], 5)) #[-1, 1, 2, 3, 4]

    print(triplet_sum_list_smaller_than_target([-1, 0, 2, 3], 3))
    print(triplet_sum_list_smaller_than_target([-1, 4, 2, 1, 3], 5))
main()
