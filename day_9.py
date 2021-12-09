def calculate_smallest_values(grid):
    smallest_values = []

    m = len(grid) - 1
    n = len(grid[0]) - 1

    risk_count = 0

    print(m, n)

    for j, row in enumerate(grid):
        for i, v in enumerate(row):
            if i == 0:
                if j == 0:
                    other_vs = [(0, 1), (1, 0)]
                elif j == m:
                    other_vs = [(m - 1, 0), (m, 1)]
                else:
                    other_vs = [(j - 1, 0), (j, 1), (j + 1, 0)]
            elif i == n:
                if j == 0:
                    other_vs = [(0, n-1), (1, n)]
                elif j == m:
                    other_vs = [(m - 1, n), (m, n-1)]
                else:
                    other_vs = [(j - 1, n), (j, n-1), (j + 1, n)]
            else:
                if j == 0:
                    other_vs = [(0, i-1), (1, i), (0, i+1)]
                elif j == m:
                    other_vs = [(m - 1, i), (m, i-1), (m, i+1)]
                else:
                    other_vs = [(j - 1, i), (j, i-1), (j, i+1), (j + 1, i)]

            smaller_count = 0

            for y, x in other_vs:
                if grid[y][x] > grid[j][i]:
                    smaller_count += 1

            if smaller_count == len(other_vs):
                print((j, i), other_vs)

                smallest_values.append((j, i))
                risk_count += v + 1

    return risk_count, smallest_values


def grid_activating(grid):
    m, n = len(grid), len(grid[0])

    bool_grid = []
    for j in range(m):
        row_grid = []
        for i in range(n):
            row_grid.append(grid[j][i] != 9)
        bool_grid.append(row_grid)

    return bool_grid


def calculate_basin(well, grid, bool_grid):
    j, i = well

    print(well, grid[j][i])
    bool_grid[j][i] = False

    well_cnt = 1

    if j - 1 >= 0:
        if bool_grid[j - 1][i] and grid[j - 1][i] > grid[j][i]:
            bool_grid[j - 1][i] = False
            fnd_cnt = calculate_basin((j - 1, i), grid, bool_grid)
            well_cnt += fnd_cnt

    if j + 1 <= len(grid) - 1:
        if bool_grid[j + 1][i] and grid[j + 1][i] > grid[j][i]:
            bool_grid[j + 1][i] = False
            fnd_cnt = calculate_basin((j + 1, i), grid, bool_grid)
            well_cnt += fnd_cnt

    if i - 1 >= 0:
        if bool_grid[j][i - 1] and grid[j][i - 1] > grid[j][i]:
            bool_grid[j][i - 1] = False
            fnd_cnt = calculate_basin((j, i - 1), grid, bool_grid)
            well_cnt += fnd_cnt

    if i + 1 <= len(grid[0]) - 1:
        if bool_grid[j][i + 1] and grid[j][i + 1] > grid[j][i]:
            bool_grid[j][i + 1] = False
            fnd_cnt = calculate_basin((j, i + 1), grid, bool_grid)
            well_cnt += fnd_cnt

    return well_cnt


def grid_searching(grid, smallest_values):
    bool_grid = grid_activating(grid)

    basins = {}
    for pair in smallest_values:
        basins[pair] = calculate_basin(pair, grid, bool_grid)

    return basins


if __name__ == "__main__":
    data = []

    with open("data/day_9.txt", 'r') as input_data:
        data = [[int(v) for v in string] for string in input_data.read().split('\n')]

    # total_risk = 0

    total_risk, smallest_values = calculate_smallest_values(data)

    basins = grid_searching(data, smallest_values[:])

    a_set = list(basins.values())
    a_set.sort()

    print(a_set[-3], a_set[-2], a_set[-1])
    print(a_set[-3] * a_set[-2] * a_set[-1])

    print(total_risk)
    print(basins)