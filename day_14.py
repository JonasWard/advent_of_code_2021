import time
# from copy import deepcopy

def apply_mapping_dict(pair_dict, base_string):
    new_string = ''
    for i, char in enumerate(base_string[1:]):
        new_string += base_string[i]
        pair_string = base_string[i] + char
        if pair_string in pair_dict:
            new_string += pair_dict[pair_string]

    new_string += base_string[-1]
    return new_string


def dict_count(pair_gen_dict, state_dict):
    new_state_dict = dict(state_dict)
    for pair, count in state_dict.items():
        new_state_dict[pair_gen_dict[pair][0]] += count
        new_state_dict[pair_gen_dict[pair][1]] += count
        new_state_dict[pair] -= count

    return new_state_dict


def construct_state_dict(start_string, pair_gen_dict):
    state_dict = dict()
    
    for key, pairs in pair_gen_dict.items():
        state_dict[key] = 0
        state_dict[pairs[0]] = 0
        state_dict[pairs[1]] = 0

    for i, char in enumerate(start_string[1:]):
        pair_string = start_string[i] + char
        if pair_string in state_dict:
            state_dict[pair_string] += 1
        else:
            state_dict[pair_string] = 1

    return state_dict


def create_pair_gen_dict(pairs):
    pair_gen_dict = {}
    for pair, char in pairs.items():
        pair_gen_dict[pair] = [pair[0]+char, char+pair[1]]

    return pair_gen_dict


def create_char_count_dict(chars, string):
    count_dict = {}
    for char in chars:
        count_dict[char] = string.count(char)

    return count_dict


def create_char_count_dict_from_pair_dict(pair_state_dict):
    char_dict = {}
    
    for pair, count in pair_state_dict.items():
        if pair[0] in char_dict:
            char_dict[pair[0]] += count
        else:
            char_dict[pair[0]] = count

    return char_dict


if __name__ == "__main__":
    pair_dict = {}
    chars = set()

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_14.txt", 'r') as data_file:
        start_string, mappings = data_file.read().split("\n\n")

        for row in mappings.split('\n'):
            a, b = row.split(' -> ')
            pair_dict[a] = b
            chars.add(b)

        for char in start_string:
            chars.add(char)

    current_state = start_string

    start_time = time.time()
    print(current_state)
    for i in range(10):
        current_state = apply_mapping_dict(pair_dict, current_state)
        count_dict = create_char_count_dict(chars, current_state)
        print(count_dict)
        print(time.time() - start_time)
        start_time = time.time()

    # char_dict = create_char_count_dict(state_dict)
    for char, count in count_dict.items():
        print("char '{}': {}".format(char, count))
    
    print(max(count_dict.values()), min(count_dict.values()))
    print(max(count_dict.values())- min(count_dict.values()))

    pair_gen_dict = create_pair_gen_dict(pair_dict)
    state_dict = construct_state_dict(start_string, pair_gen_dict)
    for i in range(40):
        state_dict = dict_count(pair_gen_dict, state_dict)


    char_dict = create_char_count_dict_from_pair_dict(state_dict)
    print(start_string)
    char_dict[start_string[-1]] += 1

    for char, count in char_dict.items():
        print("char '{}': {}".format(char, count))
    
    print(max(char_dict.values()), min(char_dict.values()))
    print(max(char_dict.values())- min(char_dict.values()))

    

    