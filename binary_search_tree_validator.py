# Given a binary tree, validate it is a binary sort tree.

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
    valid_bst = BinaryTreeNode(5)
    valid_left_node = valid_bst.insert_left(3)
    valid_left_node.insert_left(2)
    valid_left_node.insert_right(4)
    valid_right_node = valid_bst.insert_right(7)
    valid_right_node.insert_left(6)
    valid_right_node.insert_right(8)

    print(validate_binary_search_tree(valid_bst))

    invalid_bst = BinaryTreeNode(5)
    invalid_left_node = invalid_bst.insert_left(3)
    invalid_left_node.insert_left(5)  # Node is out of place
    invalid_left_node.insert_right(4)
    invalid_right_node = invalid_bst.insert_right(7)
    invalid_right_node.insert_left(6)
    invalid_right_node.insert_right(8)

    print(validate_binary_search_tree(invalid_bst))


def validate_binary_search_tree(tree_root: BinaryTreeNode):
    # Perform depth-first search, and check if each node is correct relative to it's ancestors.
    # O(n) time efficiency, O(1) space efficiency
    if tree_root is None:
        return False

    # Treat tree as stack, include expected bounds for each leaf
    nodes_and_bounds_stack = [(tree_root, -float('inf'), float('inf'))]

    while len(nodes_and_bounds_stack):
        node, lower_bound, upper_bound = nodes_and_bounds_stack.pop()

        # If not in proper place relative to ancestors, return false
        if lower_bound >= node.value or node.value >= upper_bound:
            return False

        # Add left nodes to stack with same lower bound, upper bound of this node's value
        if node.left:
            nodes_and_bounds_stack.append((node.left, lower_bound, node.value))
        # Add right bounds to stack with same upper bound, lower bound of this node's value
        if node.right:
            nodes_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True


if __name__ == "__main__":
    main()
