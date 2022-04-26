#Rever all k length sub lists even if the end is not of length k.

#TC= O(N) and SC=O(1)
def reverseKGroup(self, head, k):
    if k <= 1 or head is None:
        return head

    prev, cur = None, head

    while True:
        # The last node of the previous k sub array.
        last_node_of_previous_sublist = prev
        # The last node of the previous k sub array.
        last_node_of_current_sublist = cur

        i = 0
        temp = None
        while cur and i < k:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
            i += 1

        # check if last of previous sub is not None, if it is then this is the first k of the LL.
        if last_node_of_previous_sublist != None:
            last_node_of_previous_sublist.next = prev
        else:
            head = prev

        # Assing last node of current to its next node.
        last_node_of_current_sublist.next = cur

        if cur == None:
            break

        # Assign prev to node before cur since it gets reversed along with the k sub.
        prev = last_node_of_current_sublist

    return head

#Reverse all K length substrings expect if the end is not of lenght k.

#TC=O(N) and SC=O(1)
    def reverseKGroup(self, head, k):
        if k <= 1 or head is None:
            return head

        prev, cur, navigator = None, head, head

        while True:
            # The last node of the previous k sub array.
            last_node_of_previous_sublist = prev
            # The last node of the previous k sub array.
            last_node_of_current_sublist = cur

            # Use navigator to check if k sub lists exist.
            l = 0
            while navigator and l < k:
                navigator = navigator.next
                l += 1

            # Check is sub list if of lenght k else return the head as it's the end and we dont want to reverse.
            if l == k:
                i = 0
                temp = None
                while cur and i < k:
                    temp = cur.next
                    cur.next = prev
                    prev, cur = cur, temp
                    i += 1
            else:
                return head

            # check if last of previous sub is not None, if it is then this is the first k of the LL.
            if last_node_of_previous_sublist != None:
                last_node_of_previous_sublist.next = prev
            else:
                head = prev

            # Assing last node of current to its next node.
            last_node_of_current_sublist.next = cur

            if cur == None:
                break

            # Assign prev to node before cur since it gets reversed along with the k sub.
            prev = last_node_of_current_sublist

        return head