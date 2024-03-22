# Given an undirected graph with maximum degree D, find a graph coloring using
# at most D + 1 colors.
from typing import List


class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def main():
    a = GraphNode('a')
    b = GraphNode('b')
    c = GraphNode('c')

    a.neighbors.add(b)
    b.neighbors.add(a)
    b.neighbors.add(c)
    c.neighbors.add(b)

    graph = [a, b, c]
    degree = 2
    colored_graph = color_graph(graph, degree)
    print([node.label + " " + str(node.color) for node in colored_graph])


def color_graph(graph: List[GraphNode], degree: int):
    # Greedy approach: for each node, check each neighbor's color. Choose lowest available
    # color and fill in.
    # Time efficiency: O(n * m), where m is the number of edges. Space efficiency: O(1)

    possible_colors = set([i for i in range(0, degree + 1)])

    for node in graph:
        neighbor_colors = set([neighbor.color
                               for neighbor in node.neighbors
                               if neighbor.color is not None])
        # assign first legal color
        for color in possible_colors:
            if color not in neighbor_colors:
                node.color = color
                break

    return graph


if __name__ == '__main__':
    main()
