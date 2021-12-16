def apply_folding_operation(fold, pts):
    n_pts = set()

    for pt in pts:
        if pt[fold[0]] > fold[1]:
            new_value = 2 * fold[1] - pt[fold[0]]
            if fold[0]:
                n_pts.add((pt[0], new_value))
            else:
                n_pts.add((new_value, pt[1]))
        else:
            n_pts.add(pt)

    return n_pts


def print_grid(pts):
    xs, ys = zip(*pts)
    m, n = max(xs), max(ys)

    grid_string = ''
    for y in range(n+1):
        row_string = ''
        for x in range(m+1):
            if (x, y) in pts:
                row_string+='ø'
            else:
                row_string+=' '
        row_string+='\n'
        grid_string+=row_string

    print(grid_string)


if __name__ == "__main__":
    pts = []
    folding_operations = []

    direction_dict = {
        'x': 0,
        'y': 1
    }
    
    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_13.txt", 'r') as data_file:
        pts_string, fold_string = data_file.read().split("\n\n")
        for row in pts_string.split('\n'):
            a, b = row.split(',')
            pts.append((int(a), int(b)))

        for row in fold_string.split('\n'):
            a, b = row.strip("fold along ").split('=')
            folding_operations.append((direction_dict[a], int(b)))

    print(pts)
    print(folding_operations)

    for fold_opt in folding_operations:
        pts = apply_folding_operation(fold_opt, pts)
        
    print_grid(pts)
