import heapq
import time
from math import floor


def calculate_distances(graph, starting_vertex):
    start_time = time.time()

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

    print("duration: {}".format(time.time() - start_time))

    return distances


def neighbourhouds(position, m,n):
    values = []
    if position[0] > 0:
        values.append((position[0] - 1, position[1]))

    if position[0] < m - 1:
        values.append((position[0] + 1, position[1]))

    if position[1] > 0:
        values.append((position[0], position[1] - 1))

    if position[1] < n - 1:
        values.append((position[0], position[1] + 1))

    return values


def graph_from_grid(grid):
    m,n = len(grid[0]), len(grid)

    very_big_value = m * n * 10

    graph = {}
    for i in range(m):
        for j in range(n):
            graph[(i,j)] = dict(((a,b), grid[a][b]) for a,b in neighbourhouds((i,j), m,n))

    return graph


def scaling_grid_five_times(grid):
    m,n = len(grid[0]), len(grid)

    n_grid = []
    for i_s in range(5):
        for i in range(m):
            grid_row = []
            for j_s in range(5):
                for j in range(n):

                    loc_v = grid[i][j] + i_s + j_s
                    if loc_v > 9:
                        grid_row.append((loc_v - 1) % 9 + 1)
                    else:
                        grid_row.append(loc_v)
        
            n_grid.append(grid_row)

    return n_grid


def display_grid(grid):
    grid_string = ''

    m,n = len(grid[0]), len(grid)
    for j in range(n):
        for i in range(m):
            grid_string += str(grid[j][i])

        grid_string += '\n'

    print(grid_string)


if __name__ == "__main__":
    grid = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_15.txt", 'r') as data_file:
        grid = [[int(v) for v in row] for row in data_file.read().split("\n")]

    graph = graph_from_grid(grid)

    display_grid(grid)
    
    distances = calculate_distances(graph, (0,0))

    m,n = len(grid[0]), len(grid)
    print(distances[m-1, n-1])

    grid = scaling_grid_five_times(grid)
    display_grid(grid)

    graph = graph_from_grid(grid)
    
    distances = calculate_distances(graph, (0,0))

    m,n = len(grid[0]), len(grid)
    print(distances[m-1, n-1])
    