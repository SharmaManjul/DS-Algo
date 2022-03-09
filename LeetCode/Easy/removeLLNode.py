#This one is a weird one, instead of having access to the entire LL to delete a
#given node we are instead only given the node to delete. SO to achieve a
#similar effect we can copy the next nodes val and next into the one we want to
#delete.

def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
