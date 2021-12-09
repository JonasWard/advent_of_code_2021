def i_curtailing(i, count):
    if i == 0:
        return [], [1, 2]
    elif i == 1:
        return [0], [2, 3]
    elif i == count - 2:
        return [count - 4, count - 3], [count - 1]
    elif i == count - 1:
        return [count - 3, count - 2], []
    else:
        return [i - 2, i - 1], [i + 1, i + 2]


def finding_smallest(main_row):
    # row_min_2 = main_row[2:] + [0, 0]
    # row_min_1 = main_row[1:] + [0]
    #
    # row_max_2 = [0, 0] + main_row[:-2]
    # row_max_1 = [0] + main_row[:-1]
    #
    # row_deltas = [0 for i in range(len(main_row))]
    #
    # for row_section in [row_min_2, row_min_1, row_max_1, row_max_2]:
    #     for i, v in enumerate(row_section):
    #         row_deltas[i] += main_row[i] - v
    #
    solution_key = []

    total_risk = 0

    for i, v in enumerate(main_row):
        smaller_is, larger_is = i_curtailing(i, len(main_row))

        if len(smaller_is) == 2 and len(larger_is) == 2:
            v0, v1 = [main_row[i] for i in smaller_is]
            v2, v3 = [main_row[i] for i in larger_is]

            if (v1 < v0) and (v1 > v) and (v < v2) and (v2 < v3):
                total_risk += v + 1

        elif len(smaller_is) == 2 and len(larger_is) == 1:
            v0, v1 = [main_row[i] for i in smaller_is]
            v2 = [main_row[i] for i in larger_is][0]

            if (v1 < v0) and (v1 > v) and (v < v2):
                total_risk += v + 1

        elif len(smaller_is) == 2 and len(larger_is) == 0:
            v0, v1 = [main_row[i] for i in smaller_is]

            if (v1 < v0) and (v1 > v):
                total_risk += v + 1

        elif len(smaller_is) == 0 and len(larger_is) == 2:
            v2, v3 = [main_row[i] for i in larger_is]

            if (v < v2) and (v2 < v3):
                total_risk += v + 1

        elif len(smaller_is) == 1 and len(larger_is) == 2:
            v1 = [main_row[i] for i in smaller_is][0]
            v2, v3 = [main_row[i] for i in larger_is]

            if (v1 > v) and (v < v2) and (v2 < v3):
                total_risk += v + 1

    return total_risk


if __name__ == "__main__":
    data = []

    with open("data/day_9.txt", 'r') as input_data:
        data = [[int(v) for v in string] for string in input_data.read().split('\n')]

    total_risk = 0

    for row in data:
        # print(''.join([str(v) for v in row]))
        total_risk += finding_smallest(row)

    print(total_risk)