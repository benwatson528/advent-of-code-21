import heapq


def solve(grid):
    nodes, distances = build_graph(grid)
    visited = calculate_distances(distances)
    return visited[(len(grid) - 1, len(grid[0]) - 1)]


def calculate_distances(graph):
    starting_vertex = (0, 0)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def build_graph(grid):
    distances = {}
    nodes = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            nodes.add((i, j))
            distances[(i, j)] = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for neighbour in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[i]):
                    distances[(i, j)][neighbour] = grid[i][j]
                    distances[neighbour][(i, j)] = grid[i][j]
    return nodes, distances
