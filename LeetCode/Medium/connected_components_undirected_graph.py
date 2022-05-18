# TC = O(N) and SC = O(N)

class Grapher:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find_root(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
            self.count -= 1

    def get_connected(self):
        return self.count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = Grapher(n)

        for edge in edges:
            graph.union(edge[0], edge[1])

        return graph.get_connected()