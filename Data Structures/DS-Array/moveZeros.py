#Imput: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Space complexity = O(1) & time complexity = O(n)
#Using two pointer approach

nums = [1,3,4,5,0,0,0,7,0,6,0,3]

def moveZeros(nums):
    nonZero = 0

    for i in range(len(nums)):
        if  not (nums[i] == 0):
            nums[nonZero] = nums[i]
            nonZero += 1

    print(nonZero)

    for j in range(nonZero,len(nums),1):
        nums[j] = 0

    return nums

print(moveZeros(nums))
