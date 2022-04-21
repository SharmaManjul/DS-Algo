#TC=O(N) and SC=O(1)
def linked_list_reversor(self, node):
    left, right = node, node.next
    left.next = None
    while right:
        temp = right.next
        right.next = left
        left, right = right, temp
    return left


def reorderList(self, head):
    # Find the middle
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the LL
    tail = self.linked_list_reversor(slow)

    while tail.next:
        head_temp = head.next
        tail_temp = tail.next
        head.next = tail
        tail.next = head_temp
        head, tail = head_temp, tail_temp