from copy import deepcopy

# reading the data
def parse_bingo(file_name):
    inputs = []
    bingo_grids = []

    with open(file_name, 'r') as bingo_data:
        first_split = bingo_data.read().split('\n\n')
        
        inputs = [int(v) for v in first_split[0].split(',')]

        for bingo_string in first_split[1:]:
            cell = []
            for row in bingo_string.split('\n'):
                loc_row = []
                for v in row.split(' '):
                    if len(v) > 0:
                        loc_row.append(int(v))
                cell.append(loc_row)

            bingo_grids.append(cell)

    return inputs, bingo_grids


def apply_input(bingo_grid, bool_grid, input):
    for i, row in enumerate(bingo_grid):
        for j, v in enumerate(row):
            if input == v:
                bool_grid[i][j] = True


def has_complete_row(bool_grid):
    for row in bool_grid:
        if sum(row) == 5:
            return True

    return False


def hase_complete_column(bool_grid):
    for column in zip(*bool_grid):
        if sum(column) == 5:
            return True

    return False


def calculate_score(input_grid, bool_grid):
    score = 0

    for i, row in enumerate(input_grid):
        for j, v in enumerate(row):
            if not(bool_grid[i][j]):
                score += v

    return score


def bingo_bools():
    return [[False for i in range(5)] for j in range(5)]


def display_grid(grid):
    return '\n'.join([' '.join([str(v) for v in row]) for row in grid])


def play_bingo(bingo_grids, inputs):
    bools_bingo_grids = [bingo_bools() for _ in range(len(bingo_grids))]

    for input in inputs:
        for bingo_grid, bool_grid in zip(bingo_grids, bools_bingo_grids):
            apply_input(bingo_grid, bool_grid, input)

            if has_complete_row(bool_grid) or hase_complete_column(bool_grid):
                print(display_grid(bool_grid))
                print(display_grid(bingo_grid))
                
                return calculate_score(bingo_grid, bool_grid) * input



def loose_bingo(bingo_grids, inputs):
    boards_to_win = len(bingo_grids)

    copied_bingo_grids = deepcopy(bingo_grids)
    bools_bingo_grids = [bingo_bools() for _ in range(len(copied_bingo_grids))]

    for input in inputs:
        new_bingo_grids, new_bool_grids = [], []

        for bingo_grid, bool_grid in zip(bingo_grids, bools_bingo_grids):
            apply_input(bingo_grid, bool_grid, input)

            if not(has_complete_row(bool_grid) or hase_complete_column(bool_grid)):
                new_bingo_grids.append(bingo_grid)
                new_bool_grids.append(bool_grid)

            else:
                boards_to_win -= 1

                if boards_to_win == 0:
                    return calculate_score(bingo_grid, bool_grid) * input

        bingo_grids = new_bingo_grids
        bools_bingo_grids = new_bool_grids

if __name__ == "__main__":
    file_name = "/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_4.txt"

    inputs, bingo_grids = parse_bingo(file_name)

    print(play_bingo(bingo_grids, inputs))
    print(loose_bingo(bingo_grids, inputs))
