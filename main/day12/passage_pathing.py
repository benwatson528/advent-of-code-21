from collections import defaultdict


def solve(connections) -> int:
    graph = build_graph(connections)
    grids = find_all_paths(graph, 'start', [])
    return len(grids)


def build_graph(connections):
    graph = defaultdict(list)
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])
    return graph


def find_all_paths(graph, start, path):
    path = path + [start]
    if start == 'end':
        return [path]
    paths = []
    for node in graph[start]:
        if (node.islower() and node not in path) or node.isupper():
            paths.extend(find_all_paths(graph, node, path))
    return paths
