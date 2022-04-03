#Rotate given array by value k.

#TC=O(n) and SC=O(n)
def rotate(self, nums, k):
    if not len(nums) == 0 or not k == 0:
        s_nums = []
        for i in range(len(nums)):
            s_nums.append(nums[i])
        for j in range(len(nums)):
            # print(j, (j+k)%len(nums))
            nums[(j + k) % len(nums)] = s_nums[j]

#TC=O(n) and SC=O(1)
def rotate(self, nums, k):
    def reversor(nums, l, r):
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            r -= 1
            l += 1

    if not len(nums) == 0 or not k == 0:
        k = k % len(nums)
        reversor(nums, 0, len(nums) - k - 1)
        reversor(nums, len(nums) - k, len(nums) - 1)
        reversor(nums, 0, len(nums) - 1)