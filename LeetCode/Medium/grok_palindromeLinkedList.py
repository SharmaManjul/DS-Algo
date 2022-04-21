#TC = O(N) and SC=O(1)
def linked_list_reversor(self, node):
    left, right = node, node.next
    left.next = None
    while right:
        temp = right.next
        right.next = left
        left, right = right, temp
    return left


def isPalindrome(self, head):
    # Find the middle
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the LL
    tail = self.linked_list_reversor(slow)

    # Check if palindrome.
    while tail:
        if tail.val != head.val:
            return False
        tail = tail.next
        head = head.next
    return True

    # Rereverse the LL to it's original form.
    tail = self.linked_list_reversor(slow)