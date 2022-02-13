class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #Using the python slice operator with a T.C. of O(n) and S.C. of O(1s)
        lenNums=len(nums)
        k %= lenNums
        nums[:] = nums[lenNums-k:]+nums[:lenNums-k]

        #Brute force approach would be to make a new array that stores the values of the modified nums and
        #then reassign it to nums.
        #for loop where append all elements from k+1 t len-1 to new array and with another for loop append
        #all elements from 0 to k to the new array.
        #Finally reaasgin all the elements to nums.
        #This method has a T.C. of O(n) and a S.C. of O(n)

        #Using array reversal. When we reserve our array we notice that the elements are in the right
        #order but the subarrays ranging from 0 to k and k to len need to be resered individually.
        lenNums=len(nums)
        if(k>lenNums):
            k %= lenNums

        def reversor(nums, left, right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1

        reversor(nums, 0, lenNums-1)
        reversor(nums, 0, k-1)
        reversor(nums, k, lenNums-1)
