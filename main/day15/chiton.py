import heapq


def solve(grid, extend_grid=False):
    if extend_grid:
        grid = extend(grid)
    distances = build_graph(grid)
    visited = dijkstra(distances)
    return visited[(len(grid) - 1, len(grid[0]) - 1)]


def build_graph(grid):
    distances = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            distances[(i, j)] = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for neighbour in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[i]):
                    distances[(i, j)][neighbour] = grid[neighbour[0]][neighbour[1]]
                    distances[neighbour][(i, j)] = grid[i][j]
    return distances


# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
def dijkstra(graph):
    starting_vertex = (0, 0)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


def extend(grid):
    original_grid_size = len(grid)
    for i in range(4 * original_grid_size):
        grid.append([])
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                continue
            for m in range(original_grid_size):
                for n in range(original_grid_size):
                    new_value = (((grid[m][n] + i + j) - 1) % 9) + 1
                    grid[(i * original_grid_size) + m].append(new_value)
    return grid
