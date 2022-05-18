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
            if self.count == 1:
                return True
            else:
                return False

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friend_graph = Grapher(n)
        logs.sort()
        result = -1
        for log in logs:
            if friend_graph.union(log[1], log[2]):
                return log[0]
        return -1