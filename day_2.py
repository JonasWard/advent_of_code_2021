def import_data(file_name):
    movement_list = []

    with open(file_name, 'r') as data:
        for line in data.readlines():
            movement, delta = line.split(' ')
            movement_list.append([movement, int(delta)])

    return movement_list


def position_calculation_simple(movement_list):
    depth = 0
    distance = 0

    for movement, delta in movement_list:
        if movement == "forward":
            distance += delta
        elif movement == "down":
            depth += delta
        elif movement == "up":
            depth -= delta
        else:
            print(movement)

    return depth, distance


def position_calculation_aim(movement_list):
    depth = 0
    distance = 0
    aim = 0

    for movement, delta in movement_list:
        if movement == "forward":
            distance += delta
            depth += aim * delta
        elif movement == "down":
            aim += delta
        elif movement == "up":
            aim -= delta
        else:
            print(movement)

    return depth, distance


if __name__ == "__main__":
    movement_list = import_data("./data/day_2.csv")

    depth, distance = position_calculation_simple(movement_list)
    print(depth, distance)
    print(depth * distance)

    depth, distance = position_calculation_aim(movement_list)
    print(depth, distance)
    print(depth * distance)