# Trick is to use slow and fast pointers to detect a cycle as at some point if a cycle exists te two pointers will meet.
# The time complexity will the length of the list plus the lenght of the cycle as at most it will the pointers one cycle
# to find each other.

# TC = O(N+K) an SC = O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge case
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False