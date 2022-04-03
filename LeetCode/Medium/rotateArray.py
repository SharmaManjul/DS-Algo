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