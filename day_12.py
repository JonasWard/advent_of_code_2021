
def construct_graph(edges_tuples):
    nodes = {}

    for a,b in edges_tuples:
        if a in nodes and not(b in nodes[a]):
            nodes[a].append(b)
        else:
            nodes[a] = [b]

        if b in nodes and not(a in nodes[b]):
            nodes[b].append(a)
        else:
            nodes[b] = [a]

    return nodes


def is_small(node):
    return node.islower()


class Path:
    def __init__(self, start_node, end_node, all_nodes):
        self.nodes = [start_node]
        self.end_node = end_node
        self.reference = all_nodes

    def clone(self):
        n_path = Path(None, self.end_node, self.reference)
        n_path.nodes = self.nodes[:]
        return n_path

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def next_nodes(self):
        return self.reference[self.nodes[0]]

    def valid_next(self):
        valid_nodes = []
        for next_node in self.next_nodes():
            if not(next_node.islower() and next_node in self.nodes):
                valid_nodes.append(next_node)

        return valid_nodes


def find_paths(start_node, end_node, all_nodes):
    paths = [Path(start_node, end_node, all_nodes)]

    print(paths)

    found_new = True
    
    i = 0
    path_length = len(paths)

    final_paths = []

    n_paths = []
    while found_new:
        # print("I am here")
        for path in paths:
            # print(path)
            print(path.valid_next())

            for new_node in path.valid_next():
                n_path = path.clone()
                n_path.add_node(new_node)

                if new_node == end_node:
                    final_paths.append(n_path)
                else:
                    n_paths.append(n_path)
                

        paths = n_paths

        # print(i)
        # print(len(paths))

        i+=1

        if i > 10:
            print("exeded iteration count")
            if path_length == len(n_paths):
                found_new = False

        path_length =  len(n_paths)

    return paths


if __name__ == "__main__":
    edges_tuples = []

    with open("/Users/jonas/Documents/reps/advent_of_code_2021/data/day_12.txt", 'r') as data_file:
        edges_tuples = [tuple(row.split('-')) for row in data_file.read().split('\n')]

    nodes = construct_graph(edges_tuples)

    print(nodes)

    print("here?")

    paths_found = find_paths('start', 'end', nodes)
