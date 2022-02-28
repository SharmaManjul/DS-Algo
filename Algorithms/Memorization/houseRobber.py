#Leet code #198: House robber done using dynamic programming without recursoin.

def rob(self, nums):
    rob1 ,rob2 = 0, 0
    for item in nums:
        temp = max(item + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
