# Using slow and fast pointers to find the middle and then reversing the second half of the LL. Start combining them inplace
# we need to track the next of each of the two pointers while we perform the reorder.

# O(N)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the LL.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half.
        right = slow.next
        prev = slow.next = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        # Merge the two lists.
        left, right = head, prev
        while right:
            left_next, right_next = left.next, right.next
            left.next = right
            right.next = left_next
            left, right = left_next, right_next