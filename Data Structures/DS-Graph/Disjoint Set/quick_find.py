# UnionFind class
class UnionFind:
    def __init__(self, size):
        # Initialize array of length size with the indexes as the value. Initially the root of all elements is itself.
        self.root = [x for x in range(size)]

    def find(self, x):
        # Reuturn the value of index x since that will be its root.
        return self.root[x]

    def union(self, x, y):
        # Get the root of both x and y.
        root_x = self.find(x)
        root_y = self.find(y)
        # Check if they have differnt roots, so we will need to perform union.
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

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