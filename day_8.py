def string_filter_function(a_string):
    return len(a_string) > 0


def unique_filter_function(a_list):
    return len(a_list) == 1


state_dict = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}


def gen_len_dict(state_dict):
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


def gen_overlap_with_uniques_dict(state_dict):
    overlap_with_uniques_dict = {}

    for state, values in state_dict.items():
        loc_dict = {}
        for state_again, values_again in state_dict.items():
            if not(state_again == state):
                loc_dict[state_again] = overlap_function(values, values_again)
        overlap_with_uniques_dict[state] = loc_dict

    return overlap_with_uniques_dict


def gen_overlap_by_length(len_dict, overlap_with_uniques_dict):
    overlap_by_length = {}

    for key, values in len_dict.items():
        loc_dict = {}

        for value in values:
            for overlap_key, overlap_value in overlap_with_uniques_dict[value].items():
                if overlap_value in loc_dict:
                    if overlap_key in loc_dict[overlap_value]:
                        loc_dict[overlap_value][overlap_key].append(value)
                    else:
                        loc_dict[overlap_value][overlap_key] = [value]
                else:
                    loc_dict[overlap_value] = {overlap_key: [value]}

        overlap_by_length[key] = loc_dict

    return overlap_by_length


def search_overlap_by_length(string, solved_string, solved_strings_value, overlap_by_length):
    string_length = len(string)
    overlap_strings = overlap_function(string, solved_string)

    return overlap_by_length[string_length][overlap_strings][solved_strings_value]


def solve_output_strings(outputs, unique_value_count, unique_lens, overlap_by_length):
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

    # print("before solving based on found uniques: " + ' '.join(output_string))

    print(not_solved)
    print(solved)

    count = 20
    while any(not_solved):
        new_not_solved = not_solved[:]
        new_solved = solved[:]

        for i, string in enumerate(not_solved):
            for j, solved_string in enumerate(solved):
                keys = search_overlap_by_length(
                    string,
                    solved_string,
                    solved_strings_values[j],
                    overlap_by_length
                )

                if len(keys) == 1:
                    print(keys, i, j, solved, not_solved)
                    unique_value_count[keys[0]] += 1
                    solved_strings_values.append(keys[0])
                    new_solved.append(string)
                    new_not_solved.pop(i)

                    # print(new_not_solved)

                    print("found a new solution!")

                    break

        not_solved = new_not_solved
        solved = new_solved

        count -= 1

        print(count)

        if count < 0:
            print("over-itterated")
            break


if __name__ == "__main__":
    data = []

    with open("data/day_8.txt", 'r') as input_data:
        data = [[tuple(filter(string_filter_function, loc_data.split(' '))) for loc_data in string.split('|')] for string in input_data.read().split('\n')]

    len_dict = gen_len_dict(state_dict)

    print(len_dict)

    unique_lens = gen_unique_lens(len_dict)
    print(unique_lens)

    unique_value_count = dict((value, 0) for value in range(10))
    print(unique_value_count)

    overlap_with_uniques_dict = gen_overlap_with_uniques_dict(state_dict)
    print(overlap_with_uniques_dict)

    overlap_by_length = gen_overlap_by_length(len_dict, overlap_with_uniques_dict)

    for input_data, output_data in data:
        solve_output_strings(output_data, unique_value_count, unique_lens, overlap_by_length)

    print(unique_value_count)
    print(sum(unique_value_count.values()))

    for input_data, output_data in data:
        solve_output_strings(input_data, unique_value_count, unique_lens, overlap_by_length)
