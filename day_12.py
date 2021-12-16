
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


def recurse_paths(nodes, start_node, end_node):
    found_new_nodes = True

    while:
        break



if __name__ == "__main__":
    edges_tuples = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_12.txt", 'r') as data_file:
        edges_tuples = [tuple(row.split('-')) for row in data_file.read().split('\n')]

    print(construct_graph(edges_tuples))
