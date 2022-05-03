#TC=O(N) and SC=O(N)

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.max_diameter = 0

    def diameter_finder(node):
        #returns 0 is node is None, help us get the height of a leaf node.
        if not node:
            return 0

        #Grab the left and right height associated to a node.
        l_height = diameter_finder(node.left)
        r_height = diameter_finder(node.right)

        #The diameter is the left height plus the right height, here we are counting the links as a measurement of diameter.
        cur_diameter = l_height + r_height

        #Check if new diameter greater than max
        self.max_diameter = max(self.max_diameter, cur_diameter)

        #Return the height of the node above the one we are on, return the max of left and right and add 1 to it so we
        #account for the additional link to the parent node.
        return max(l_height, r_height) + 1

    diameter_finder(root)
    return self.max_diameter