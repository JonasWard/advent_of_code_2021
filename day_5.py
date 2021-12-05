def parse_lines(file_name):
    lines = []

    with open(file_name, 'r') as bingo_data:
        for txt_line in bingo_data.readlines():
            # print(txt_line)
            pt_a, pt_b = txt_line.split('->')
            x0, y0 = pt_a.strip(' \n').split(',')
            x1, y1 = pt_b.strip(' \n').split(',')

            lines.append([(int(x0), int(y0)), (int(x1), int(y1))])

    return lines


def line_horizontal(ln):
    return ln[0][1] == ln[1][1]


def line_vertical(ln):
    return ln[0][0] == ln[1][0]


def min_x(line):
    return min(line[0][0], line[1][0])


def max_x(line):
    return max(line[0][0], line[1][0])


def min_y(line):
    return min(line[0][1], line[1][1])


def max_y(line):
    return max(line[0][1], line[1][1])


def add_pt_to_dict(pt, pts_dict):
    if pt in pts_dict:
        pts_dict[pt] += 1
    else:
        pts_dict[pt] = 1


def get_pts_on_line(line, pts_dict):
    if line_horizontal(line):
        y = line[0][1]
        for x in range(min_x(line), max_x(line) + 1, 1):
            add_pt_to_dict( (x, y), pts_dict)

    elif line_vertical(line):
        x = line[0][0]
        for y in range(min_y(line), max_y(line) + 1, 1):
            add_pt_to_dict( (x, y), pts_dict)

    else:
        # case is diagonal line
        (x0, y0), (x1, y1) = line

        if x0 < x1:
            x_step = 1
        else:
            x_step = -1

        if y0 < y1:
            y_step = 1
        else:
            y_step = -1

        delta = abs(y1 - y0) + 1

        print(delta, (x_step, y_step), line)

        for i in range(delta):
            add_pt_to_dict( (int(x0 + i * x_step), int(y0 + i * y_step)), pts_dict)
            

if __name__ == "__main__":
    file_name = "/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_5.txt"

    lines = parse_lines(file_name)

    pt_dictionary = {}

    ln_cnt = 0
    for line in lines:
        get_pts_on_line(line, pt_dictionary)

    double_hit_cnt = 0

    for v in pt_dictionary.values():
        if v > 1:
            double_hit_cnt += 1

    print(double_hit_cnt)
    