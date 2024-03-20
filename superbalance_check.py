# Given a binary tree, determine if the tree is "superbalanced." A tree is superbalanced
# if the difference between the depths of any two leaf nodes is no greater than one.


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def main():
    superbalanced_tree = BinaryTreeNode(1)
    left_leaf = superbalanced_tree.insert_left(2)
    left_leaf.insert_left(3)
    left_leaf.insert_right(4)
    right_leaf = superbalanced_tree.insert_right(5)
    right_leaf.insert_left(6)

    print(check_if_superbalanced(superbalanced_tree))

    unbalanced_tree = BinaryTreeNode(1)
    unbalanced_left_leaf = unbalanced_tree.insert_left(2)
    unbalanced_bot_left_left = unbalanced_left_leaf.insert_left(3)
    unbalanced_left_leaf.insert_right(4)
    unbalanced_bot_left_left.insert_left(5).insert_left(6).insert_left(8)  # depth of 3
    unbalanced_tree.insert_right(7)  # depth of 1

    print(check_if_superbalanced(unbalanced_tree))


def check_if_superbalanced(tree_root: BinaryTreeNode):
    # Depth- and breadth-first traversals will both have the same worst-case.
    # This specific algorithm may short-circuit when hitting leaves, so depth-first
    # should increase the average case.

    # Perform depth-first search and track leaf depths. Return false if a subsequent leaf has
    # 2 less depth than the max.

    if tree_root is None:
        return True

    leaf_depths = []  # tracker. short circuit if we find more than 2 different depths

    nodes = [(tree_root, 0)]

    while len(nodes):
        node, depth = nodes.pop()

        # Case: current node is a leaf
        if not node.left and not node.right:
            if depth not in leaf_depths:
                leaf_depths.append(depth)

            # Check for balance
            if len(leaf_depths) > 2:
                return False
            if len(leaf_depths) == 2:
                if abs(leaf_depths[0] - leaf_depths[1]) > 1:
                    return False

        # Case: current node is not a leaf. Step down and increase depth
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True


if __name__ == "__main__":
    main()
