# UnionFind class
# Here the TC is <= O(N) and if we want to find the union of N elements our TC will be <=O(N^2) whereas the TC for quick
# find will always be fixed to O(N^2), Therefore union find is more efficient.
class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]

    def find(self, x):
        # The value at x is not necessarily the root as it can be just the parent of the value. So
        # to find the root we need to navigate until the index value is equal to the value at the index.
        while x != self.root[
            x]:  # Loop until the value of index is euqal to the value at the index ie. the root vertex.
            x = self.root[x]
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.root[x] == self.root[y]


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