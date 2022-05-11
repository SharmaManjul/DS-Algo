# TC = O(N * logK) where N is number of elements and K is the number of lists, SC = O(K)

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    min_heap = []
    # Add first root node val and list index to min heap and move the node to next so that when we access the list node
    # it is already on the next.
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, [lists[i].val, i])
            lists[i] = lists[i].next

    # Initialize head of our output and using a pointer cur,
    head = ListNode(None)
    cur = head
    # Pop heap element and initialize cur.next with it's val and point cur to cur.next. Chech if the node on list index
    # i is not None and if so push val and index to heap and point list node to next.
    while min_heap:
        val, index = heapq.heappop(min_heap)
        cur.next = ListNode(val)
        cur = cur.next

        if lists[index]:
            heapq.heappush(min_heap, [lists[index].val, index])
            lists[index] = lists[index].next

    return head.next