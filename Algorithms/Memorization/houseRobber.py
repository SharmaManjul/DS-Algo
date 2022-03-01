#Leet code #198: House robber done using dynamic programming without recursion.

def rob(self, nums):
    rob1 ,rob2 = 0, 0
    for item in nums:
        temp = max(item + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

# Done using DP and recursion.
    def rob(self, nums):
        rob1 ,rob2, i = 0, 0, -1

        def robbing(rob1, rob2, i, nums):
            if i == len(nums)-1:
                return rob2
            else:
                print(rob2)
                i+=1
            return robbing(rob2, max(nums[i]+rob1, rob2), i, nums)

        return robbing(rob1, rob2, i, nums)
