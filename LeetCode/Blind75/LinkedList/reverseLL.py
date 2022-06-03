# Store prev node attributes while traversing so we will always have the cur node and prev node at hand to preform
# reversal.
# TC = O(N)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        node = head

        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        return prev_node