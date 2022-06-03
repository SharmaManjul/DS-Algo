# Idea is that if we maintain n distance between our two pointers while traversing the LL. Once
# the pointer hits the end of the list we will know for sure that the other pointer is at the
# head of the node we want to delete.

# O(N)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case
        if not head or n < 0:
            return None

        result = ListNode()
        result.next = head
        first_node, second_node = result, result
        # Move second node n away from first.
        for _ in range(n):
            second_node = second_node.next

        # Keep traversing while maintaining n gap till second is at the end.
        while second_node.next:
            first_node = first_node.next
            second_node = second_node.next

        # First node is the head of the node we want to remove.
        first_node.next = first_node.next.next

        return result.next