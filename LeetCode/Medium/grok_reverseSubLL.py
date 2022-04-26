#TC=O(N) and SC=O(1)
def reverseBetween(self, head, left, right):
    # Find when to reverse the LL an also track the last node of reversed LL.

    i = 1
    cur, prev = head, None

    while cur and i < left:
        prev = cur
        cur = cur.next
        i += 1

    last_node_before_left = prev
    last_node_of_reversed_LL = cur

    i = 0
    while cur and i < right - left + 1:
        temp = cur.next
        cur.next = prev
        prev, cur = cur, temp
        i += 1

    if last_node_before_left:
        last_node_before_left.next = prev
    else:
        head = prev

    last_node_of_reversed_LL.next = cur

    return head
