def read_file(file_name):
    initial_states = []

    with open(file_name, 'r') as ints:
        initial_states = [int(state) for state in ints.read().strip('\n ').split(',')]

    return initial_states


def empty_bracket_dict():
    return dict([(i, 0) for i in range(9)])


def bracketing(initial_states):
    bracket_dict = empty_bracket_dict()

    for state in initial_states:
        bracket_dict[state] += 1

    return bracket_dict


def iterate_brackets(bracket_dict):
    n_bracket_dict = empty_bracket_dict()

    for i, value in bracket_dict.items():
        if i == 0:
            n_bracket_dict[6] += value
            n_bracket_dict[8] += value

        else:
            n_bracket_dict[i - 1] += value

    return n_bracket_dict


def iterate(states):
    new_states = []

    for state in states:
        if state == 0:
            new_states.append(6)
            new_states.append(8)

        else:
            new_states.append(state - 1)

    return new_states


if __name__ == "__main__":
    states = read_file("./data/day_6.txt")

    bracket_dict = bracketing(states)

    for i in range(256):
        bracket_dict = iterate_brackets(bracket_dict)

    print(sum(bracket_dict.values()))