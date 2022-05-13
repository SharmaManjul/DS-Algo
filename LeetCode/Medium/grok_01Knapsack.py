# Brute force approach usinf recursive calls for each combination possible.
# TC = O(2^N) and SC = O(N)
# def solve_knapsack(profits, weights, capacity):
#     result = profit_finder(profits, weights, capacity, 0)
#     return result
#
# def profit_finder(profits, weights, capacity, index):
#     # Base Check
#     if index == len(profits):
#         return 0
#
#     profit1, profit2 = 0, 0
#     # Including the item at the index
#     if weights[index] <= capacity:
#         profit1 = profit_finder(profits, weights, capacity-weights[index], index+1) + profits[index]
#
#     # Ignoring the item at the index
#     profit2 = profit_finder(profits, weights, capacity, index + 1)
#
#     # Return the max of the two profits.
#     return max(profit1, profit2)
#
# def main():
#     print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
#     print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
#
# main()



# Using memoization to not re-calculate sub problems.
# TC: O(N * C) where N is the number of items and C is the capacity. We will only perform recursive calls
# for our N items till te capacity runs out.
# SC: O(N + N*C) N for the recursive stack and the N*C for the hash map.

# def solve_knapsack(profits, weights, capacity):
#     result = profit_finder(profits, weights, capacity, 0, {})
#     return result
#
# def profit_finder(profits, weights, capacity, index, profit_map):
#     # Base Check
#     if index == len(profits):
#         return 0
#
#     if (capacity, index) in profit_map:
#         return profit_map[(capacity, index)]
#
#     profit1, profit2 = 0, 0
#     # Including the item at the index
#     if weights[index] <= capacity:
#         profit1 = profit_finder(profits, weights, capacity-weights[index], index+1, profit_map) + profits[index]
#
#     # Ignoring the item at the index
#     profit2 = profit_finder(profits, weights, capacity, index + 1, profit_map)
#
#     # Return the max of the two profits.
#     profit_map[(capacity, index)] = max(profit1, profit2)
#     return profit_map[(capacity, index)]
#
# def main():
#     print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
#     print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
#
# main()



# Bottom up approach using dynamic programming.
# TC = O(N*C) and SC = O(N*C)
def solve_knapsack(profits, weights, capacity):
    # Edge cases
    index_len = len(profits)
    if capacity <= 0 or index_len == 0  or index_len != len(weights):
        return 0

    # 2-Dimensional list to store the table with x axis as the capacities starting from 0 and y axis as the indexes
    # starting at 0.
    knapsack_list = [[x for x in range(capacity+1)] for y in range(index_len)]

    # Loop through the 2-d array while filling up the table. Whenever the capacity is 0 we know that we can't add any items
    # so default set the profit to 0. Also when the index is 0 and the wweight of that index is less than or equal to the
    # capacity we can add the same profit for index 0 for  all capacities. Then we want find two profits, one if the weight
    # of the current index is less than or equal to the capacity then we add that to the profit of the previous index at the
    # capacity minus the current weight, after this we will have the profit associated to the current item and the items before.
    # Now we calculate the profit if the current element was not included ie the profit of the previous index at full capacity.
    # We store the max of these two elements at the kanpsack table and return the last element of this table as the result.

    for i in range(index_len):
        for c in range(capacity+1):
            profit1, profit2 = 0, 0

            if c == 0:
                knapsack_list[i][c] = 0

            if i == 0 and weights[i] <= c:
                knapsack_list[i][c] = profits[i]

            if weights[i] <= c:
                profit1 = profits[i] + knapsack_list[i-1][c-weights[i]]

            profit2 = knapsack_list[i-1][c]

            knapsack_list[i][c] = max(profit1, profit2)

    return knapsack_list[index_len-1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()



# Bottom up approach using dynamic programming and printing out the selected weights.
# TC = O(N*C) and SC = O(N*C)
def solve_knapsack(profits, weights, capacity):
    # Edge cases
    index_len = len(profits)
    if capacity <= 0 or index_len == 0  or index_len != len(weights):
        return 0

    # 2-Dimensional list to store the table with x axis as the capacities starting from 0 and y axis as the indexes
    # starting at 0.
    knapsack_list = [[x for x in range(capacity+1)] for y in range(index_len)]

    for i in range(index_len):
        for c in range(capacity+1):
            profit1, profit2 = 0, 0

            if c == 0:
                knapsack_list[i][c] = 0

            if i == 0 and weights[i] <= c:
                knapsack_list[i][c] = profits[i]

            if weights[i] <= c:
                profit1 = profits[i] + knapsack_list[i-1][c-weights[i]]

            profit2 = knapsack_list[i-1][c]

            knapsack_list[i][c] = max(profit1, profit2)

    weights_printer(profits, weights, capacity, knapsack_list)

    return knapsack_list[index_len-1][capacity]

def weights_printer(profits, weights, capacity, knapsack_list):
    print("The selected weights were: ")
    n = len(profits)
    total_profit = knapsack_list[n-1][capacity]
    for i in range(n-1, 0, -1):
        if total_profit !=  knapsack_list[i-1][capacity]:
            print(weights[i], " , ")
            total_profit -= profits[i]
            capacity -= weights[i]

    if total_profit != 0:
        print(weights[0])




def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()

