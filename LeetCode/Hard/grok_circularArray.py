#TC=O(N^2) since we have nested loops and SC= O(N)
def get_next_item(self, prev_direction, nums, cur_index):
    # Checking if there is change in direction.
    cur_direction = nums[cur_index] >= 0
    if cur_direction != prev_direction:
        return -1

    next_index = (cur_index + nums[cur_index]) % len(nums)

    # Chekcing if there is single element cycle.
    if next_index == cur_index:
        return -1

    return next_index


def circularArrayLoop(self, nums):
    for i in range(len(nums)):
        # True is forward and False is backward.
        cur_direction = nums[i] >= 0
        slow, fast = i, i

        while True:
            slow = self.get_next_item(cur_direction, nums, slow)
            fast = self.get_next_item(cur_direction, nums, fast)
            if fast != -1:
                fast = self.get_next_item(cur_direction, nums, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True
    return False

#If you maintain a hash map of all the number that don't result in cycles then we cna reduce the TC to O(N) as we would
# only need to loop once through the array but that would mean our SC is now O(N).
class Solution(object):

    def get_next_item(self, prev_direction, nums, cur_index, seen):
        # Checking if there is change in direction.

        cur_direction = nums[cur_index] >= 0
        if cur_direction != prev_direction:
            seen[cur_index] = True
            return -1

        next_index = (cur_index + nums[cur_index]) % len(nums)

        # Chekcing if there is single element cycle.
        if next_index == cur_index:
            seen[cur_index] = True
            return -1

        return next_index

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        for i in range(len(nums)):
            # True is forward and False is backward.
            cur_direction = nums[i] >= 0
            slow, fast = i, i

            if i in visited:
                continue

            while True:
                slow = self.get_next_item(cur_direction, nums, slow, visited)
                fast = self.get_next_item(cur_direction, nums, fast, visited)
                if fast != -1:
                    fast = self.get_next_item(cur_direction, nums, fast, visited)

                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True
        return False