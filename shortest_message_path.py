# Given a dictionary representing an unweighted adjacency graph, find the shortest
# path from one node to another.
from collections import deque
from typing import List


def main():
    adjacency_graph = {
        'Mike': ['Whiskey', 'Juliett', 'Oscar'],
        'Whiskey': ['Mike', 'November'],
        'Juliett': ['Mike', 'Alpha', 'Romeo', 'November'],
        'Romeo': ['Juliett', 'Oscar'],
        'Alpha': ['Juliett', 'Tango', 'Delta'],
        'Tango': ['Alpha', 'Delta', 'Sofia', 'Lucas'],
        'Delta': ['Alpha', 'Tango', 'Liam', 'November'],
        'November': ['Juliett', 'Whiskey'],
        'Oscar': ['Romeo', 'Mike']
    }

    solution = find_shortest_path('Tango', 'Juliett', adjacency_graph)  # Expect Tango, Alpha, Juliett
    print([node for node in solution])


def find_shortest_path(start: str, end: str, adjacency_graph: dict[str, List[str]]) -> List[str]:
    # Fastest route through an unweighted graph is always a breadth-first search.
    # Basic BFS has to be modified here to also maintain a "shortest path" to each
    # node visited so far, to backtrack through and return when end node is found.

    # Time efficiency: O(n * m), where m is number of connections between users.
    # Space efficiency: O(n) worst-case, for shortest path to all nodes.
    nodes_to_visit = deque()
    nodes_to_visit.append(start)
    shortest_path_to_nodes = {start: None}

    while len(nodes_to_visit):
        current_node = nodes_to_visit.popleft()
        if end in adjacency_graph.get(current_node):
            shortest_path_to_nodes[end] = current_node
            break
        for neighbor in adjacency_graph.get(current_node):
            if neighbor not in shortest_path_to_nodes:
                shortest_path_to_nodes[neighbor] = current_node
                nodes_to_visit.append(neighbor)

    # If no route is possible, throw error
    if not shortest_path_to_nodes.get(end):
        raise Exception('No possible route to end.')

    # Iterate backwards through route and return
    path = [end]
    while path[-1] is not start:
        path.append(shortest_path_to_nodes.get(path[-1]))
    path.reverse()
    return path


if __name__ == '__main__':
    main()
