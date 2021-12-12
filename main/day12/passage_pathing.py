from collections import Counter, defaultdict


def solve_unlimited(connections) -> int:
    graph = build_graph(connections)
    paths = find_all_paths(graph, 'start', [])
    return len(paths)


def solve_limited(connections) -> int:
    graph = build_graph(connections)
    paths = find_all_paths_limit(graph, 'start', [])
    return len(paths)


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


def find_all_paths_limit(graph, start, path):
    path = path + [start]
    if start == 'end':
        return [path]
    paths = []
    for node in graph[start]:
        if is_valid_movement(node, path):
            paths.extend(find_all_paths_limit(graph, node, path))
    return paths


def is_valid_movement(current, path):
    counter = Counter(x for x in path if x.islower() and x != current and x != 'start')
    # We can only visit start once
    if current == 'start' and len(path) == 1:
        return True
    elif current == 'start':
        return False
    # We can visit uppers as often as we want
    elif current.isupper():
        return True
    # You can visit any lowercase node once
    elif current.islower() and path.count(current) == 0:
        return True
    # One lower can be visited twice, the others only once
    elif current.islower() and path.count(current) < 2 and 2 not in counter.values():
        return True
    return False
