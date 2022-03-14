#Contruct a pascal triangle given the number of rows.

#Using two for loops with TC=O(n) and SC=O(n)
def generate(self, numRows):
    res = [[1]]
    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        newRow = []
        for j in range(len(res[-1]) + 1):
            newRow.append(temp[j] + temp[j + 1])
        res.append(newRow)
    return res