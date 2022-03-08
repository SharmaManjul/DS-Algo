#Iterative approach
def reverseList(self, head):
    left = head
    if head == None or head.next == None:
        return head
    right = left.next
    while right:
        tmp = right.next
        right.next = left
        left = right
        right = tmp
    head.next = None
    head = left
    return head

#Recursive approach
def reverseList(self, head):
    def reverser(head, new):
        if not head:
            return new
        nex = head.next
        head.next = new
        return(reverser(nex, head))
return reverser(head, None)
