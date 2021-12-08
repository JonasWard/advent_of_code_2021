data = []

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

len_dict = {}

for key, values in state_dict.items():
    if len(values) in len_dict:
        len_dict[len(values)].append(key)
    else:
        len_dict[len(values)] = [key]

unique_lens = {}

for cnt, keys in len_dict.items():
    if len(keys) == 1:
        unique_lens[cnt] = keys[0]

def overlap_function(string_list_a, string_list_b):
    cnt = 0
    for v_a in string_list_a:
        if v_a in string_list_b:
            cnt += 1

    return cnt


overlap_with_uniques_dict = {}

for state, values in state_dict.items():
    loc_dict = {}
    for state_again, values_again in state_dict.items():
        if not(state_again == state):
            loc_dict[state_again] = overlap_function(values, values_again)
    overlap_with_uniques_dict[state] = loc_dict

print(overlap_with_uniques_dict)

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

print(overlap_by_length)


with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_8.txt", 'r') as input_data:
    data = [[list(filter(string_filter_function, data.split(' '))) for data in string.split('|')] for string in input_data.read().split('\n')]

unique_value_count = dict((value, 0) for value in unique_lens.values())

def search_overlap_by_length(string, solved_string, overlap_by_length):
    pass

def solve_output_strings(outputs, unique_value_count, unique_lens, overlap_by_length):
    output_string = []
    solved = []
    not_solved = []

    # filtering the unique ones
    for string in outputs:

        if len(string) in unique_lens:

            solved.append(string)
            unique_value_count[unique_lens[len(string)]] += 1
            output_string.append(str(unique_lens[len(string)]))

        else:

            not_solved.append(string)
            output_string.append(string)

    print("before solving based on found uniques: " + ' '.join(output_string))

    count = 20
    while any(not_solved):
        for string in not_solved:
            for solved_string in solved:
                pass



for input_data, _ in data:
    solve_output_strings(input_data, unique_value_count, unique_lens, overlap_by_length)

print(unique_value_count)
print(sum(unique_value_count.values()))
