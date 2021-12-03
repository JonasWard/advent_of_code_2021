from copy import deepcopy

def import_data(file_name):
    line_grid = []

    with open(file_name, 'r') as data:
        for line in data.readlines():
            loc_line = []
            for value in line:
                if (value == '1'):
                    loc_line.append(True)
                elif (value == '0'):
                    loc_line.append(False)

            line_grid.append(loc_line)

    return line_grid


def grid_count(grid):
    v_lengths = [0 for i in range(len(grid[0]))]

    for line in grid:
        for i, v in enumerate(line):
            if v:
                v_lengths[i] += 1

    return v_lengths


def grid_index_count(grid, index):
    cnt = 0

    for line in grid:
        if line[index]:
            cnt += 1

    return cnt


def filter_grid(grid, index, value = True):
    filtered_grid = []

    for line in grid:
        if line[index] == value:
            filtered_grid.append(line)

    return filtered_grid


def filter_by_cnt_for_index(grid, for_largest = True, on_draw = True, index = 0):
    value = grid_index_count(grid, index)

    if value * 2 == len(grid):
        filter_value = on_draw
    else:
        filter_value = (value * 2 > len(grid)) == for_largest

    return filter_grid(grid, index, filter_value)


def filter_by_cnt(grid, for_largest = True, on_draw = True):
    filtered_grid = deepcopy(grid)

    for i in range(len(grid[0])):
        filtered_grid = filter_by_cnt_for_index(filtered_grid, for_largest, on_draw, i)

        if len(filtered_grid) == 1:
            break

    if len(filtered_grid) == 1:
        return filtered_grid[0]


def bools_to_int(b_list):
    v_string = ''.join([str(int(v)) for v in b_list])

    return int(v_string, 2)


def values(counted_grid, half_count):
    gamma_rate = [v < half_count for v in counted_grid]
    epsilon_rate = [not(v) for v in gamma_rate]

    epsilon_int = bools_to_int(epsilon_rate)
    gamma_int = bools_to_int(gamma_rate)

    return epsilon_int, gamma_int


if __name__ == "__main__":
    line_grid = import_data("./data/day_3.csv")

    half_count = int(len(line_grid) * .5)

    counted_grid = grid_count(line_grid)

    epsilon_int, gamma_int = values(counted_grid, half_count)

    print("epsilon: ", epsilon_int)
    print("gamma: ", gamma_int)

    print(epsilon_int * gamma_int)

    o_2_bitrate = filter_by_cnt(line_grid, for_largest=True, on_draw=True)
    co_2_bitrate = filter_by_cnt(line_grid, for_largest=False, on_draw=False)

    o_int = bools_to_int(o_2_bitrate)
    co_2_int = bools_to_int(co_2_bitrate)


    # o_int, co_2_int = bools_to_int(o_2_bitrate), bools_to_int(co_2_bitrate)

    print("o2: ", o_int)
    print("co2: ", co_2_int)

    print(o_int * co_2_int)
