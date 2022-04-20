#TC = O(N) and SC=O(1)
def middleNode(self, head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow