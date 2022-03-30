#Check if linked list has a cycle in it.

#Using while loop and a hash set with TC = O(n) and SC = O(n)

def hasCycle(self, head):
    hashSet = {}
    while head != None:
        if head in hashSet:
            return True
        else:
            hashSet[head] = True
            head = head.next
    return False