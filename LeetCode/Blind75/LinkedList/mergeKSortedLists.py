#Use the fact that 2-way merge of 2 lists at a time is more efficient than one by one. Loop through list combining the LL's two at a time.
# TC = O(N*logK) and SC = O(1)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge Case
        if not lists or len(lists) == 0:
            return None

        def list_merge(l1, l2):
            merged_list = ListNode()
            cur_node = merged_list
            while l1 and l2:
                if l1.val < l2.val:
                    cur_node.next = l1
                    l1 = l1.next
                else:
                    cur_node.next = l2
                    l2 = l2.next
                cur_node = cur_node.next
            if l1:
                cur_node.next = l1
            if l2:
                cur_node.next = l2
            return merged_list.next

        while len(lists) > 1:
            merged_result = []
            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i + 1] if i < (len(lists) - 1) else None
                merged_result.append(list_merge(list_1, list_2))
            lists = merged_result
        return lists[0]