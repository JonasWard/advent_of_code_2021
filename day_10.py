from statistics import median

VALID_CHARACTER_PAIRS = ['{}', '[]', '()', '<>']
START_CHARACTERS = dict((a, b) for a, b in VALID_CHARACTER_PAIRS)
END_CHARACTERS = dict((b, a) for a, b in VALID_CHARACTER_PAIRS)
INCREASE_DECREASE = {}
CHAR_PAIR = {}

ILLEGAL_CHARACTER = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

for i, key in enumerate(START_CHARACTERS.keys()):
    INCREASE_DECREASE[key] = 1
    CHAR_PAIR[key] = VALID_CHARACTER_PAIRS[i]

for i, key in enumerate(END_CHARACTERS.keys()):
    INCREASE_DECREASE[key] = -1
    CHAR_PAIR[key] = VALID_CHARACTER_PAIRS[i]


def string_chunking(string, start_idx = 0):
    chunks = []

    print(string)

    if any(string):
        chunks.append(string[0])
        end_character = START_CHARACTERS[string[0]]

        f_idx = string.find(end_character)

        if f_idx > -1:
            chunks.append(string_chunking(string[1:f_idx - 1], start_idx + 1))
            chunks.append(string_chunking(string[f_idx:]), start_idx + f_idx)

            chunks.append(end_character)

        else:
            chunks.append(string_chunking(string[1:], start_idx + 1))

    return chunks


def depth_map(string):
    global_states = {0: 0}
    specific_states = dict((subString, 0) for subString in VALID_CHARACTER_PAIRS)

    for i, char in enumerate(string):
        global_states[i+1] = global_states[i] + INCREASE_DECREASE[char]
        specific_states[CHAR_PAIR[char]] += INCREASE_DECREASE[char]

    return global_states, specific_states


def read_string(string):
    expected_closed = [START_CHARACTERS[string[0]]]

    for i, char in enumerate(string[1:]):
        if char in START_CHARACTERS:
            expected_closed.append(START_CHARACTERS[char])
        elif char == expected_closed[-1]:
            expected_closed.pop()
        else:
            return False, i+1, char, expected_closed[-1]

    closing_char = '' if not(any(expected_closed)) else expected_closed[-1]

    return True, 0, char, closing_char


def auto_complete_string(string):
    expected_closed = [START_CHARACTERS[string[0]]]

    for i, char in enumerate(string[1:]):
        if char in START_CHARACTERS:
            expected_closed.append(START_CHARACTERS[char])
        elif char == expected_closed[-1]:
            expected_closed.pop()
        else:
            return False, i + 1, char, expected_closed[-1]

    return expected_closed


AUTO_COMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


if __name__ == "__main__":
    data = []

    with open("data/day_10.txt", 'r') as input_data:
        data = [string for string in input_data.read().split('\n')]

    error_score = 0

    new_strings = []

    for string in data:
        success, index, char, expected_char = read_string(string)

        if not(success):
            print(index, len(string))
            error_score += ILLEGAL_CHARACTER[char]
        else:
            new_strings.append(string)

        # print(success, index, char, expected_char)

    print(error_score)

    total_scores = []

    for string in new_strings:
        missing_parts = auto_complete_string(string)
        missing_parts.reverse()

        loc_score = 0

        for char in missing_parts:
            loc_score *= 5
            loc_score += AUTO_COMPLETE[char]

        total_scores.append(loc_score)

    print(median(total_scores))