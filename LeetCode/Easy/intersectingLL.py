#Find where the LL intersect with each other and return that node.

#Using hashmap: TC=O(n) and SC=O(n)
def getIntersectionNode(self, headA, headB):
    mapA = {}
    while headA:
        mapA[headA] = True
        headA = headA.next
    while headB:
        if headB in mapA:
            return headB
        headB = headB.next

#Using two pointers that switch heads when None is encountered this brings them to the same level and offsets the length
#difference.
#TC=O(n+m) and SCO(1)
def getIntersectionNode(self, headA, headB):
    pA = headA
    pB = headB
    while pA != pB:
        if pA == None:
            pA = headB
        else:
            pA = pA.next
        if pB == None:
            pB = headA
        else:
            pB = pB.next
    return pA