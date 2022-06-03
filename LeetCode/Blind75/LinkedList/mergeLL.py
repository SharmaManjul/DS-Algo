# Use dummy node to point to the first element in the merged list. Compare the node of the two lists and pick the smaller
# one to add to the merge list. Since we are doing inplace just use the dummy node to traverse and manipulate the next of
# the nodes to create a merged list.

# O(M+N) where M & N are lengths of the lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        result = ListNode()
        res_node = result
        while list1 and list2:
            if list1.val < list2.val:
                res_node.next = list1
                list1 = list1.next
            else:
                res_node.next = list2
                list2 = list2.next
            res_node = res_node.next
        if list1:
            res_node.next = list1
        else:
            res_node.next = list2
        return result.next