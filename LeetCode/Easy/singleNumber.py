#136: Find the single number in a list of number pairs, TC has to be O(n) and
#SC O(constant)

#Set approach with TC=O(n) and SC= O(n)
def singleNumber(self, nums):

    found = set()
    for num in nums:
        if num in found:
            found.remove(num)
        else:
            found.add(num)
    return found.pop()

#XOR approach with TC=O(n) and SC=O(1)
def singleNumber(self, nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor
