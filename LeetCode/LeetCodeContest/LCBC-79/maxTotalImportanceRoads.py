# To many unnecessary DS used but solution is reached.
# TC = O(NlogN) and SC = O(N)

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_roads = [0] * n

        for road in roads:
            city_roads[road[0]] += 1
            city_roads[road[1]] += 1

        max_heap = []
        for city in range(len(city_roads)):
            heapq.heappush(max_heap, (-city_roads[city], city))

        city_importance = [0] * n
        importance_val = n
        while max_heap:
            _, city = heapq.heappop(max_heap)
            city_importance[city] = n
            n -= 1

        max_importance = 0
        for road in roads:
            max_importance += city_importance[road[0]] + city_importance[road[1]]

        return max_importance

# Instead of tracking which city has has what value just multiply the freq with the importance values. Since all the values
# are added the number of time the number of roads so we can just multiply the freq of roads from a city times the value
# of the city.

# TC = O(NlogN) and SC = O(N)

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_roads = [0] * n
        for road in roads:
            city_roads[road[0]] += 1
            city_roads[road[1]] += 1
        city_roads.sort()
        print(city_roads)
        max_importance = 0
        for i in range(n):
            max_importance += city_roads[i] * (i + 1)

        return max_importance