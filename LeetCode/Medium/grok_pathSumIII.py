#TC = O(N * log(N)) for balanced tree and TC = O(N^2) for skewed trees
#SC = O(N)

def pathSum(self, root, targetSum):

    def sum_finder(node, path_list):
        if not node:
            return 0

        #Maintain a list of the path we are traversing.
        path_list.append(node.val)

        path_sum, path_count = 0, 0
        #Loop the path list from the back and check is any of the sums are the target and if true then increament count.
        for i in range(len(path_list) - 1, -1, -1):
            path_sum += path_list[i]

            if path_sum == targetSum:
                path_count += 1

        #traverse the tree in dfs fashion while adding all the path counts from all possible paths and subpaths.
        path_count += sum_finder(node.left, path_list)
        path_count += sum_finder(node.right, path_list)

        path_list.pop()

        return path_count