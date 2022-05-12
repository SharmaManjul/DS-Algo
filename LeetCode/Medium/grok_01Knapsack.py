# Brute force approach usinf recursive calls for each combination possible.
# TC = O(2^N) and SC = O(N)
def solve_knapsack(profits, weights, capacity):
    result = profit_finder(profits, weights, capacity, 0)
    return result

def profit_finder(profits, weights, capacity, index):
    # Base Check
    if index == len(profits):
        return 0

    profit1, profit2 = 0, 0
    # Including the item at the index
    if weights[index] <= capacity:
        profit1 = profit_finder(profits, weights, capacity-weights[index], index+1) + profits[index]

    # Ignoring the item at the index
    profit2 = profit_finder(profits, weights, capacity, index + 1)

    # Return the max of the two profits.
    return max(profit1, profit2)

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()