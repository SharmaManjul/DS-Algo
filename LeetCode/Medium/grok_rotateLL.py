#TC = O(N) and SC=O(1)

def rotateRight(self, head, k):
    if k <= 0 or head == None or head.next == None:
        return head

    # Find the lenght of the LL and also the last node of the LL.
    last_node = head
    list_len = 1
    while last_node.next:
        last_node = last_node.next
        list_len += 1

    # Find the the true k, no need to rotate more than len.
    k %= list_len

    if k == list_len or list_len == 1:
        return head

    # Point last node to head to make it a circular LL.
    # Since the LL will be split in the middle the old tail and head need to be connected.
    last_node.next = head
    skip_len = list_len - k
    new_last_node = head
    for i in range(skip_len - 1):
        new_last_node = new_last_node.next

    head = new_last_node.next
    new_last_node.next = None

    return head