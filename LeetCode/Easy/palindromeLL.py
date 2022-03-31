#Check if LinkedList is a palindrome

#Converting LL into a list and then checking if palindrome. TC=O(n) and SC=O(n)
def isPalindrome(self, head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    k = len(nums) - 1
    for i in range(0, len(nums) / 2):
        if nums[i] != nums[k]:
            return False
        k -= 1
    return True

#Optimized solution: TC=O(n) and SC=O(1)
def isPalindrome(self, head):
     #Find the middle node.
    slow, fast = head, head
     while fast and fast.next:
         slow =  slow.next
         fast = fast.next.next
    #Reverse the other half
    left, right = slow, slow.next
     left.next = None
     while right:
        temp = right.next
        right.next = left
        left, right = right, temp
    #Check if LL is a palindrome
     while left:
        if head.val != left.val:
            return False
        head, left = head.next, left.next
     return True