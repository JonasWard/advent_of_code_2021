import time
import heapq

class Node:
    def __init__(self, position, weight, distance, grid_dim, previous = None):
        self.p = position
        self.w = weight
        self.d = distance
        self.pre = previous
        
        self.g_m, self.g_n = grid_dim

    def neighbourhoud_grid(self):
        values = []
        if self.p[0] > 0:
            values.append((self.p[0] - 1, self.p[1]))

        if self.p[0] < self.g_m - 1:
            values.append((self.p[0] + 1, self.p[1]))

        if self.p[1] > 0:
            values.append((self.p[0], self.p[1] - 1))

        if self.p[1] < self.g_n - 1:
            values.append((self.p[0], self.p[1] + 1))

        return values


    @staticmethod
    def node_with_smallest_distance(nodes):
        zipped = zip(nodes, [node.d for node in nodes])
        nodes, _ = zip(*sorted(zipped, key=lambda x: x[1]))

        return nodes[0]


def dijkstra(grid):
    start_time = time.time()
    m,n = len(grid[0]), len(grid)

    print(m,n)

    very_big_value = m * n * 10

    nodes_grid = []
    nodes = []
    for i in range(m):
        nodes_grid_row = []
        for j in range(n):
            node = Node((i, j), grid[i][j], very_big_value, (m,n))
            nodes.append(node)
            nodes_grid_row.append(node)

        nodes_grid.append(nodes_grid_row)

    nodes[0].d = 0

    source = nodes[0]
    target = nodes[- 1]

    iteration = 1

    while nodes:
        closest_node = Node.node_with_smallest_distance(nodes)

        nodes.remove(closest_node)

        for i,j in closest_node.neighbourhoud_grid():
            loc_node = nodes_grid[i][j]

            if loc_node in nodes:
                new_distance = closest_node.d + loc_node.w
                if new_distance < loc_node.d:
                    loc_node.d = new_distance
                    loc_node.pre = loc_node

        iteration += 1

        # print(iteration)

    print(target.d)
    print(target.d)

    print("duration: {}".format(time.time() - start_time))




if __name__ == "__main__":
    grid = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_15.txt", 'r') as data_file:
        grid = [[int(v) for v in row] for row in data_file.read().split("\n")]
    
    dijkstra(grid)