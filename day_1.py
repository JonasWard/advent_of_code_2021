def increment_count(data):
    increments = 0

    for i in range(len(data) - 1):
        increments += data[i] < data[i+1]

    return increments


def increment_3sum_count(data):
    increments = 0

    for i in range(len(data) - 3):
        overlap = data[i+1] + data[i+2]
        increments += data[i] + overlap < overlap + data[i+3]

    return increments


def import_data(file_name):
    int_list = []

    with open(file_name, 'r') as data:
        for line in data.readlines():
            int_list.append(int(line))

    return int_list


if __name__ == "__main__":
    int_list = import_data("./data/day_1.csv")

    print(increment_count(int_list))
    print(increment_3sum_count(int_list))