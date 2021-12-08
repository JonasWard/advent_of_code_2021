from statistics import median, mean
from math import inf

def read_file(file_name):
    initial_states = []

    with open(file_name, 'r') as ints:
        initial_states = [int(state) for state in ints.read().strip('\n ').split(',')]

    return initial_states


def calculate_distance(states, delta):
    cnt = 0

    for state in states:
        cnt += abs(state - delta)

    return cnt


def calculate_distance_delta(states, delta):
    cnt = 0

    for state in states:
        n = abs(state-delta)
        cnt += int( n * .5 * (1 + n))

    return cnt


if __name__ == "__main__":
    states = read_file("./data/day_7.txt")

    print(states)
    median_value = int(median(states))

    value_cnt = inf
    smallest_value = 0

    for i in range(-10, 11, 1):
        loc_value = calculate_distance(states, median_value + i)

        if loc_value < value_cnt:
            value_cnt = loc_value
            smallest_value = median_value + i

    print(smallest_value, value_cnt)

    average_value = int(mean(states))

    value_cnt = inf
    smallest_value = 0

    print(average_value)

    for i in range(-10, 10, 1):
        loc_value = calculate_distance_delta(states, average_value + i)

        if loc_value < value_cnt:
            value_cnt = loc_value
            smallest_value = average_value + i

    print(smallest_value, value_cnt)