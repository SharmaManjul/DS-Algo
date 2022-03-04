#Reverse string given as array of characters in place without using extra memory
#T.C. = O(n/2) and S.C. = O(1) 

def reverseString(self, s):

    left, right = 0, len(s)-1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        right-=1
        left+=1
    print(s)
