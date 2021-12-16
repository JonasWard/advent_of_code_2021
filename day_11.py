FLASH_COUNT = 0

def boundary_mask(i, j, m, n):
    i_start = i-1 if i-1 >= 0 else 0
    i_stop = i+2 if i+2 <= m else m

    i_s = range(i_start, i_stop, 1)

    j_start = j-1 if j-1 >= 0 else 0
    j_stop = j+2 if j+2 <= n else n

    j_s = range(j_start, j_stop, 1)

    jjs = []
    for i_v in i_s:
        for j_v in j_s:
            jjs.append([i_v, j_v])

    # print(i, j, list(i_s), list(j_s), jjs, m, n)

    return jjs


def cca(grid):
    global FLASH_COUNT

    n_grid = []

    m, n = len(grid[0]), len(grid)

    for row in grid:
        n_grid.append([(v + 1) for v in row])

    flashes_grid = [[0 for i in range(m)] for j in range(n)]

    for j, row in enumerate(n_grid):
        for i, v in enumerate(row):
            if v > 9:
                FLASH_COUNT += 1
                for loc_i, loc_j in boundary_mask(i, j, m, n):
                    flashes_grid[loc_j][loc_i] += 1
    
    new_flashes = True
    
    while new_flashes:
        new_flashes = False
        for j, row in enumerate(n_grid):
            for i, v in enumerate(row):
                loc_v = flashes_grid[j][i] + v
                if loc_v > 9 and not(v > 9):
                    flashes_grid[j][i] = 0
                    n_grid[j][i] = loc_v

                    FLASH_COUNT += 1
                    new_flashes = True

                    for loc_i, loc_j in boundary_mask(i, j, m, n):
                        flashes_grid[loc_j][loc_i] += 1

    for j, row in enumerate(n_grid):
        for i, v in enumerate(row):
            loc_v = flashes_grid[j][i] + v
            flashes_grid[j][i] = loc_v if loc_v < 10 else 0

    return flashes_grid


def repr_grid(grid):
    return '\n'.join([''.join([str(v) for v in row]) for row in grid])


if __name__ == "__main__":
    grid_data = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_11.txt") as input_data:
        for string in input_data.read().split('\n'):
            grid_data.append([int(char) for char in string])

    print(repr_grid(grid_data))

    for i in range(1000):
        grid_data = cca(grid_data)

        if sum([sum(row) for row in grid_data]) == 0:
            print(i)
            break

    print(FLASH_COUNT)
