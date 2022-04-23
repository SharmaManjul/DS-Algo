#TC=O(M+N) and SC=(N+M)
def intervalIntersection(self, firstList, secondList):
    i, j, start, end = 0, 0, 0, 1
    res = []

    while i < len(firstList) and j < len(secondList):
        first_inside_second = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
        second_inside_first = firstList[i][0] <= secondList[j][0] and secondList[j][0] <= firstList[i][1]

        if first_inside_second or second_inside_first:
            res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return res