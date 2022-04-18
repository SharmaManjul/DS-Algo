from collections import deque

#The trick is to use a deque to add valid elements to the front and add it to the result array because when we add to
#the front we can avoid duplicates.

#TC=O(N^3) and SC=O(N^2), SC is that since the deque will only be O(N) at max but the worst for the output array is all
#the contiguous subarray which for each i for that contiguous array we will have n-1, n-2 ...+1 ways to choose j. Which
#gives us n+(n-1)+(n-2)+...+2+1 => n*(n-1)/2 which is O(N^2)
def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        print(left, right)
        prod_list = deque()
        for i in range(right, left-1, -1):
            prod_list.appendleft(arr[i])
            print(prod_list)
            result.append(list(prod_list))
            print(result)

    return result


def main():

    print(find_subarrays([2, 5, 3, 10], 30))
    # print(find_subarrays([8, 2, 6, 5], 50))


main()