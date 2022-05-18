# TC = O(N) and SC = O(N
# Test case: [[0,1],[1,2],[2,3],[1,3],[1,4]]

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

    def is_tree(self):
        # If the count is not equal to 1 then we have multiple trees.
        print(self.count)
        if self.count != 1:
            return False
        else:
            return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case
        if n == 0:
            return False

        # If len of edges is more than or equal to the given size then we have a loop
        if len(edges) >= n:
            return False

        tree_graph = UnionFind(n)
        for edge in edges:
            tree_graph.union(edge[0], edge[1])

        return tree_graph.is_tree()
