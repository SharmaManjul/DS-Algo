# UnionFind class
# TC for find(): O(logN), union(): O(logN) and connected(): O(logN)
class UnionFind:
    def __init__(self, size):
        # Rank is height of the tree.
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # Same as find for quick union.
        while x != self.root[x]:
            x = self.root[x]
        return self.root[x]

    def union(self, x, y):
        # Here we want to change the root of the smaller tree to the bigger one and increase rank
        # if we encounter same height trees.
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.root[y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[x] = root_y
        else:
            self.root[x] = root_y
            self.rank[root_y] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true