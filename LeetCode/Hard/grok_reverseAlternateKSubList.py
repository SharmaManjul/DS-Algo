from __future__ import print_function
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_alternate_k_elements(head, k):
    prev, cur = None, head

    while True:
        last_node_of_previous_part = prev
        last_node_of_current_part = cur

        i = 0
        while cur and i < k:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
            i += 1

        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = prev
        else:
            head = prev

        last_node_of_current_part.next = cur

        prev = last_node_of_current_part

        #Once you reverse k sublist go ahead and skip th next k sublist.
        j = 0
        while cur and j < k:
            prev = cur
            cur = cur.next

        if cur == None:
            break

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
