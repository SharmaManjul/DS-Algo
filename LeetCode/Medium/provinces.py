# TC = O(N^2) and SC = O(N)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
            self.count -= 1

    def get_provinces(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Edge case
        if not isConnected:
            return 0
        # loop thorugh and check all cities

        n = len(isConnected)
        city_union = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    city_union.union(row, col)
        return city_union.get_provinces()