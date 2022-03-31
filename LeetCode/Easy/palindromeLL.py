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

