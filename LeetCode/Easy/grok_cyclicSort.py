# TC = O(N) + O(N-1) which is O(N) since at worst case the loop will swap N-1 element and then increment the index till N.
# SC = (1)
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            temp = nums[nums[i]-1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()