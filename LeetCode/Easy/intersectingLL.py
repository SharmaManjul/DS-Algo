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