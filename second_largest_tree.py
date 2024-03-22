# Given a binary search tree, find the second-largest element,

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
    balanced_tree = BinaryTreeNode(5)
    left_node = balanced_tree.insert_left(3)
    left_node.insert_left(2)
    left_node.insert_right(4)
    right_node = balanced_tree.insert_right(7)
    right_node.insert_left(6)
    right_node.insert_right(8)

    print(find_second_largest_element(balanced_tree))  # Expect 7

    unbalanced_tree = BinaryTreeNode(5)
    left_node = unbalanced_tree.insert_left(2)
    left_node.insert_left(1)
    left_right_node = left_node.insert_right(3)
    left_right_node.insert_right(4)

    print(find_second_largest_element(unbalanced_tree)) # Expect 4

    all_left_tree = BinaryTreeNode(5)
    depth_one_left = all_left_tree.insert_left(4)
    depth_two_left = depth_one_left.insert_left(3)
    depth_two_left.insert_left(2)

    print(find_second_largest_element(all_left_tree))  # Expect 4


def find_second_largest_element(search_tree: BinaryTreeNode):
    # On a balanced tree, 2nd largest element will be the parent of the bottom-right-most node.
    # If top node is largest element, 2nd largest element will either be its left child
    # (if child has no right node) or the bottom-right-most child of the top-node's left child.

    # O(lg(n)) time on balanced tree, O(n) time on unbalanced tree. O(1) space efficiency.

    parent_node = None

    # Handle case where top node is the largest element.
    if search_tree.right is None:
        search_tree = search_tree.left
        # Find bottom-right most node off of left branch and return value
        while search_tree.right is not None:
            search_tree = search_tree.right
        return search_tree.value

    # Handle case where top node is not the largest element. Find bottom-right most node, while
    # tracking the parent. Return parent.
    while search_tree.right is not None:
        parent_node = search_tree
        search_tree = search_tree.right
    return parent_node.value


if __name__ == '__main__':
    main()
