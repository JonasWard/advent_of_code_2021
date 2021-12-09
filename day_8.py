def string_filter_function(a_string):
    return len(a_string) > 0


def unique_filter_function(a_list):
    return len(a_list) == 1


state_dict = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

dict_state = dict((value, key) for key, value in state_dict.items())


def gen_len_dict():
    global state_dict
    len_dict = {}

    for key, values in state_dict.items():
        if len(values) in len_dict:
            len_dict[len(values)].append(key)
        else:
            len_dict[len(values)] = [key]

    return len_dict


def gen_unique_lens(len_dict):
    unique_lens = {}

    for cnt, keys in len_dict.items():
        if len(keys) == 1:
            unique_lens[cnt] = keys[0]

    return unique_lens


def overlap_function(string_list_a, string_list_b):
    cnt = 0
    for v_a in string_list_a:
        if v_a in string_list_b:
            cnt += 1

    return cnt


def gen_overlap_with_uniques_dict():
    global state_dict
    overlap_with_uniques_dict = {}

    for state, values in state_dict.items():
        loc_dict = {}
        for state_again, values_again in state_dict.items():
            if not(state_again == state):
                loc_dict[state_again] = overlap_function(values, values_again)
        overlap_with_uniques_dict[state] = loc_dict

    return overlap_with_uniques_dict


def solve_output_strings(outputs, unique_value_count, unique_lens):
    output_string = []
    solved = []
    solved_strings_values = []
    not_solved = []

    # filtering the unique ones
    for string in outputs:

        if len(string) in unique_lens:

            solved.append(string)
            unique_value_count[unique_lens[len(string)]] += 1
            output_string.append(str(unique_lens[len(string)]))
            solved_strings_values.append(unique_lens[len(string)])

        else:

            not_solved.append(string)
            output_string.append(string)


def key_sort_strings(strings):
    value_dict = {}

    for string in strings:
        length = len(string)

        if length in value_dict:
            value_dict[length].append(string)

        else:
            value_dict[length] = [string]

    return value_dict


def solving(value_dict, base_map):
    base_map['a'] = value_dict[3][0].strip(value_dict[2][0])

    solved = base_map['a']

    loc_cnt_map = dict((v, 0) for v in "abcdefg")

    for string in value_dict[5] + value_dict[2] + value_dict[3] + value_dict[4]:
        for v in string:
            loc_cnt_map[v] += 1

    for v, cnt in loc_cnt_map.items():
        if cnt == 1:
            base_map['e'] = v
            solved += v
        elif cnt == 2:
            base_map['b'] = v
            solved += v
        elif cnt == 4:
            if v in value_dict[4][0]:
                base_map['d'] = v
                solved += v

    loc_cnt_map = dict((v, 0) for v in "abcdefg")

    for string in value_dict[6]:
        for v in string:
            loc_cnt_map[v] += 1

    for v, cnt in loc_cnt_map.items():
        if cnt == 2 and not(v in solved):
            base_map['c'] = v
            solved += v

    base_map['f'] = value_dict[2][0].strip(base_map['c'])
    solved += base_map['f']

    base_map['g'] = "abcdefg".strip(solved)


def solve_strings(strings):
    global state_dict

    value_dict = key_sort_strings(strings)

    base_map = dict((v, '') for v in "abcdefg")

    solving(value_dict, base_map)

    return base_map


def map_output(map_dict, output_string):
    loc_list = [map_dict[v] for v in output_string]
    loc_list.sort()
    return dict_state[''.join(loc_list)]


def map_strings(map_dict, output_strings):
    string = ''

    for output_string in output_strings:
        string += str(map_output(map_dict, output_string))

    return int(string)


if __name__ == "__main__":
    data = []

    with open("data/day_8.txt", 'r') as input_data:
        data = [[tuple(filter(string_filter_function, loc_data.split(' '))) for loc_data in string.split('|')] for string in input_data.read().split('\n')]

    len_dict = gen_len_dict()
    unique_lens = gen_unique_lens(len_dict)

    unique_value_count = dict((value, 0) for value in range(10))
    overlap_with_uniques_dict = gen_overlap_with_uniques_dict()

    cnt = 0

    for input_data, output_data in data:
        solve_output_strings(output_data, unique_value_count, unique_lens)
        string_map = solve_strings(input_data)
        map_string = dict((value, key) for key, value in string_map.items())

        cnt += map_strings(map_string, output_data)

    print(unique_value_count)
    print(sum(unique_value_count.values()))
    print(cnt)
