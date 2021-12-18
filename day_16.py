from math import floor


class Package:
    def __init__(self, version, id, string):
        self.version = version
        self.id = id
        if id == 4:
            self.data, self.remainder = Package.value_string_parser(string)
        else:
            self.data, self.remainder = Package.package_string_parser(string)
    
    @property
    def value(self):
        if self.id == 4:
            return int(self.data, 2)
        else:
            return None

    def to_json(self):
        if self.id == 4:
            return {
                'version': self.version,
                'id': self.id,
                'data': self.id,
                'value': self.value
            }

        else:
            return {
                'version': self.version,
                'id': self.id,
                'data': self.id
            }

    @staticmethod
    def package_string_parser(string):
        packages = []

        if string[0] == '1':
            package_count = int(string[1:12], 2)
            
            active_string = string[12:]

            for i in range(package_count):
                new_package = Package.from_bit_string(active_string)
                packages.append(new_package)
                active_string = new_package.remainder
        
        else:
            packages_string = int(string[1:16], 2)
            active_string = string[16:]

            while Package.bit_string_is_valid_package(active_string):
                new_package = Package.from_bit_string(active_string)
                packages.append(new_package)
                active_string = new_package.remainder

        return packages, active_string

    @staticmethod
    def value_string_parser(string):
        data = ''
        
        while len(string) > 4:
            data += string[1:5]
            start_bit = string[0]

            string = string[5:]

            if start_bit == '0':
                break
        
        return int(data, 2), string

    @staticmethod
    def from_bit_string(bit_string):
        return Package(
            int(bit_string[:3], 2),
            int(bit_string[3:6], 2),
            bit_string[6:]
        )

    @staticmethod
    def bit_string_is_valid_package(bit_string):
        return len(bit_string) > 10


HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def to_bit_string(string):
    global HEX_MAP
    n_string = ''
    
    for char in string:
        n_string += HEX_MAP[char]

    return n_string


def string_cutter(string, slice_length = 5):
    sub_strings = []

    segment_cnt = int(floor(len(string) / slice_length))

    for i in range(segment_cnt):
        sub_strings.append(string[i * slice_length: (i+1) * slice_length])

    return sub_strings


def deconstruct_bit_string(bit_string):
    string_object = {
        'version': int(bit_string[:3], 2),
        'id': int(bit_string[3:6], 2),
        'data': []
    }

    if string_object['id'] == 4: #means it's a literal
        string_object['data'] = string_cutter(bit_string[6:])
        string_object['literal'] = data_parsing(string_object['data'])
        string_object['value'] = int(string_object['literal'], 2)

    else: #means it's a command
        string_object['lengthTypeID'] = bit_string[6] == '1'

        if string_object['lengthTypeID']:
            package_count = int(bit_string[7:18], 2)
            string_object['packageLength'] = int(floor(len(bit_string[18:])/package_count))
        
        else:
            string_object['packageLength'] = int(bit_string[7:22], 2)

        string_object['packages'] = string_cutter(bit_string[22:], string_object['packageLength'])            

    return string_object


def data_parsing(packages):
    literal = ''

    for i, p in enumerate(packages):
        if i < (len(packages) - 1):
            if p[0] != '1':
                print("faulty package {}".format(p[0]))
            
            literal += p[1:]
        
        else:
            if p[0] != '0':
                print("faulty package {}".format(p[0]))
            
            literal += p[1:]

    return literal


if __name__ == "__main__":
    strings = []
    data_objects = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_16.txt", 'r') as input_data:
        for row in input_data.readlines():
            row = row.strip('\n')
            strings.append(row)
            bit_string = to_bit_string(row)
            data_objects.append(deconstruct_bit_string(bit_string))

    print(strings)
    print(data_objects)