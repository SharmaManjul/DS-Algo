class Node:
    def __init__(self, value):
        self.left = null;
        self.right = null;
        self.value = value;

class BinarySearchTree:
    def __init__(self, value):
        self.root = null;

    def insert(value):
        //Code here

    def lookUp(value):
        //Code here

        // remove

tree = BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
JSON.stringify(traverse(tree.root))

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
