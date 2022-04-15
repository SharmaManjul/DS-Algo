#Trick is to fill squares array in reverse.

#TC = O(N) and SC=O(N)
def sortedSquares(self, nums):
    squares = [0 for i in range(len(nums))]

    biggest_square_index = len(squares) - 1

    left = 0
    right = len(nums) - 1

    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            squares[biggest_square_index] = left_sq
            left += 1
        else:
            squares[biggest_square_index] = right_sq
            right -= 1

        biggest_square_index -= 1

    return squares