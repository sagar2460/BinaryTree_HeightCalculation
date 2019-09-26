class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)


#                                    1
#                                  /   \
#                                 2     3
#                                / \    /
#                               4   5  6
#                              /       / \
#                             7       8   9

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.left.left.left = Node(7)
tree.root.right.left.left = Node(8)
tree.root.right.left.right = Node(9)

print(tree.height(tree.root))
