# Recursively with memoization.
# TC = O(N^2) and SC = O(N)
def numTrees(self, n: int) -> int:
    return self.tree_finder(n, {})

def tree_finder(self, n, n_map):
    if n in n_map:
        return n_map[n]
    if n <= 1:
        return 1
    count = 0
    # Loop through every element while computing possible left and right sub tree combinations.
    for i in range(1, n + 1):
        left_sub_tree = self.tree_finder(i - 1, n_map)
        right_sub_tree = self.tree_finder(n - i, n_map)
        # Number of ways you can combine the left and right subtree.
        count += left_sub_tree * right_sub_tree

    n_map[n] = count
    return count

# Bottom up approach by solving for each number of nodes until desired nodes is acheived. Also using cache to reuse outputs.
# TC = O(N^2) and SC = O(N)
    def numTrees(self, n: int) -> int:
        # Build list containing all no. of BST until n

        num_tree = [1 for _ in range(n + 1)]

        # We already know that 0 nodes have only 1 tree possible and 1 node has only 1 tree possible so no need
        # to compute that and we can start from 2.
        for i in range(2, n + 1):
            # For every no. of node use older values to get new number and store in total.
            total = 0
            # Loop through all possible values of root nodes and calculate their totals individually and add.
            for j in range(1, i + 1):
                left_tree_nodes = j - 1
                right_tree_nodes = i - j

                total += num_tree[left_tree_nodes] * num_tree[right_tree_nodes]

            # Add total number of trees for given number to num_tree
            num_tree[i] = total

        print(num_tree)
        return num_tree[n]
