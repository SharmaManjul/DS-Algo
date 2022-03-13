#Merge two linked list and output the head of the new merged list.

#Iteratively with TC=O(n) and SC=O(n)
def mergeTwoLists(self, list1, list2):
    newNode = ListNode()
    head = newNode

    while list1 and list2:
        if list1.val < list2.val:
            newNode.next = list1
            list1 = list1.next
        else:
            newNode.next = list2
            list2 = list2.next
        newNode = newNode.next
    newNode.next = list1 or list2

    return head.next

