# Solution by manually filling the map with every possible value.
# TC = O(N+N+N) = O(N) and SC = O(N)
class Solution:
    def digitCount(self, num: str) -> bool:
        num_map = {}
        for n in num:
            num_map[n] = 1 + num_map.get(n, 0)
        for i in range(len(num)):
            if str(i) not in num_map:
                num_map[str(i)] = 0

        print(num_map)
        for i in range(len(num)):
            if int(num[i]) != num_map[str(i)]:
                return False
        return True

# Solution using counter or hashmap.
# TC = O(N) and SC = O(N)
class Solution:
    def digitCount(self, num: str) -> bool:
        num_map = Counter(num)
        for i in range(len(num)):
            if int(num[i]) != num_map.get(str(i), 0):
                return False
        return True