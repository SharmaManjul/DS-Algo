# Idea is to use a monotonic queue with stores numbers in decreasing order. We can use this to our advantage
# as the max element for every sub list will the first element of the queue however we will nee to maintain this
# state of the queue. Whenever we add a num to the queue we need to check if that num is less than the num on
# the rightmost index of the queue. If not then we pop until we find a num greatre or queue is empty and then
# add the num. When the sub list size is k we need to add the leftmost num in queue to the result and increament
# left pointer. When the left pointer is not equal to the leftmost num of queue wepop from left.
# Use the same logic up store indexes in queue.

# TC = O(N) and SC = O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_queue = deque()
        left, right, res = 0, 0, []

        while right < len(nums):
            # Add nums to queue monotonically.
            while window_queue and nums[right] > nums[window_queue[-1]]:
                window_queue.pop()
            window_queue.append(right)

            # When l is shifted we need to rearrange queue if the l was the max ie at index 0.
            if left > window_queue[0]:
                window_queue.popleft()

            if right + 1 >= k:
                res.append(nums[window_queue[0]])
                left += 1
            right += 1

        return res