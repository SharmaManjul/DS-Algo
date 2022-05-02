class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root, sum):
    cur_path = []
    all_paths = []
    #return path_counter(root, sum, 0)
    paths_finder(root, sum, cur_path, all_paths)
    return all_paths

#Number of all paths.
#TC = O(N) and SC = O(N)
def path_counter(root, sum, counter):
    if not root:
        return 0

    if not root.left and not root.right and root.val == sum:
        counter += 1
        return counter

    return path_counter(root.left, sum-root.val, counter) + path_counter(root.right, sum-root.val, counter)

#Find list of all paths.
#Recurssion: Here the trick is to use two lists, one to keep track of current path and the other to store all paths that
#succeed. The current path need to be appended with every node val and the all paths only when the node is a leaf and
#sum is equal to val is equal to the desired sum else ecursively call the left child first and then right child. The
#recursive stack will resolve itself as we return nothing when sum not found and add path to list if found so in this case
#the recursive stack is goign to traverse all the nodes no matter what. Once the if else is resolved i.e we either found path
#or not we want to remove the last element from current list since it is no longer needed.

#TC=O(N^2) since O(N) to traverse the tree and for each leaf node we might have to append it's entire path which in worst
#case could be O(N).
#SC=O(N) + O(N * logN) for worst case since we need to store the recurssion stack and the final_list for all leaf nodes O(N)
#and each leaf node can be of height O(logN).g
def paths_finder(root, sum, cur_path, all_paths):
    if not root:
        return

    cur_path.append(root.val)

    if not root.left and not root.right and root.val == sum:
        all_paths.append(list(cur_path))
    else:
        paths_finder(root.left, sum-root.val, cur_path, all_paths)
        paths_finder(root.right, sum-root.val, cur_path, all_paths)

    del cur_path[-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
    ": " + str(find_paths(root, sum)))


main()
