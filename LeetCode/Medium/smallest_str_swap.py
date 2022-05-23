# TC = O(P)*a(V)+O(V)*a(V)+O(NlogN) = O(P+N)*a(N) + O(NlogN)
# SC = O(N)

class Grapher:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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

    def get_graph(self):
        return self.root


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        result = []
        str_graph = Grapher(len(s))  # O(N)

        for pair in pairs:  # O(P)
            str_graph.union(pair[0], pair[1])  # O(a)

        # Create groups of swappable characters using default dict which lets us initialize empty lists at values.
        groups = defaultdict(list)

        # Go through the string and set the key as its root and append the character to the list.
        for i in range(len(s)):  # O(V)
            groups[str_graph.find_root(i)].append(s[i])  # O(a)

        # Sort the lists associated to the root in reverse order so we can pop the smallest element.
        for key in groups.keys():
            groups[key].sort(reverse=True)  # O(NlogN)

        # Loop through the string, for each charcter find the root and and pop the list related to the root in the map.
        for i in range(len(s)):
            result.append(groups[str_graph.find_root(i)].pop())

        return "".join(result)