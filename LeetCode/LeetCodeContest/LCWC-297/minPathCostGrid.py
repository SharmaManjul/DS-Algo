# What do we need to do? Need to find the all the minimum costs of the paths from each first row element. Once we have all the costs pick
# the minimum cost.

# In order to find the min costs from each first row element we will use djkistra's algo which states that in
# order to find the min cost path we need to relax the each path one at a time. So starting with every first row
# element we need to find the min path possible to all the next row elements. Recusively repeat this process for
# the rest of the rows until we reach the last row and return the min cost obtained. So in total we are looking
# for two min values: first the min path for each first row element to the last and then the min path possible
# from all the first row element to the last and this value will be our answer.

# Time Complex: O(r*c*c) where r is rows and c is columns. Recursice stack is the number of rows and the loop is number of columns. The cahce helps reduce repeated computation and reduces TC.
# Space Complex: O(r*c) space required for the recursive stack.


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # Method to find min cost path for a given starting element i.e. indexes. Using LRU cache to reduce
        # repeated computation of thr same path costs.
        @lru_cache
        def min_path_finder(r, c):
            # If last row then we want to just output the element value as there is no paths possible.
            if r >= len(grid) - 1:
                return grid[r][c]

            min_cost = float('inf')

            # Recursively find the cost of each possible path for given element.
            for j in range(len(grid[0])):
                cur_cost = grid[r][c] + moveCost[grid[r][c]][j] + min_path_finder(r + 1, j)
                min_cost = min(min_cost, cur_cost)

            return min_cost

        min_path_cost = float('inf')

        for c in range(len(grid[0])):
            cur_path_cost = min_path_finder(0, c)
            min_path_cost = min(min_path_cost, cur_path_cost)

        return min_path_cost


# Using tabular DP approah.
# TC = O(m * n^2) and SC = O(m * n)

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(column)] for _ in range(row)]

        # Setting last row of dp to the element value as there are no paths possible.
        for c in range(column):
            dp[row - 1][c] = grid[row - 1][c]

        for r in range(row - 2, -1, -1):
            for c in range(column):
                for k in range(column):
                    cur_cost = grid[r][c] + moveCost[grid[r][c]][k] + dp[r + 1][k]
                    min_cost = min(dp[r][c], cur_cost)
                    dp[r][c] = min_cost

        return min(dp[0])