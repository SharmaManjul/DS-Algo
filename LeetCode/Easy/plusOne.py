#Given list of digits return list with plus one added to the number that the list makes.

#TC=O(n) and SC=O(n
class Solution(object):
    def plusOne(self, digits):
        num, res = 0, []
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - (i + 1))

        num += 1

        for n in str(num):
            res.append(n)

        return res