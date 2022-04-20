#TC = O(N) and SC = O(1)
    def cycle_len_finder(self, slow):
        cur_node = slow
        cycle_len = 0
        while True:
            cur_node = cur_node.next
            cycle_len += 1
            if cur_node == slow:
                break
        return cycle_len

    def first_cycle_node_finder(self, cycle_len, head):
        first_node, second_node = head, head

        for i in range(cycle_len):
            second_node = second_node.next

        while first_node != second_node:
            first_node = first_node.next
            second_node = second_node.next

        return first_node

    def detectCycle(self, head):
        fast, slow = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_len = self.cycle_len_finder(slow)
                return self.first_cycle_node_finder(cycle_len, head)
        return None