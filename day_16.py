class Package:
    def __init__(self, version, id, string):
        self.version = version
        self.id = id
        if id == 4:
            self.data, self.remainder = Package.value_string_parser(string)
        else:
            self.data, self.remainder = Package.package_string_parser(string)
    
    def value(self):
        if self.id == 4:
            return int(self.data, 2)
        elif self.id == 0:
            return sum(d.value() for d in self.data)
        elif self.id == 1:
            value = 1
            for d in self.data:
                value *= d.value() * 1
            return value
        elif self.id == 2:
            return min(d.value() for d in self.data)
        elif self.id == 3:
            return max(d.value() for d in self.data)
        elif self.id == 5:
            if len(self.data) > 1:
                return int(self.data[0].value() > self.data[1].value())
            else:
                print("non complete entry")
                return 0
        elif self.id == 6:
            if len(self.data) > 1:
                return int(self.data[0].value() < self.data[1].value())
            else:
                print("non complete entry")
                return 0
        elif self.id == 7:
            if len(self.data) > 1:
                return int(self.data[0].value() == self.data[1].value())
            else:
                print("non complete entry")
                return 0

    def to_json(self):
        if self.id == 4:
            return {
                "version": self.version,
                "id": self.id,
                "data": self.data,
                "value": self.value()
            }

        else:
            return {
                "version": self.version,
                "id": self.id,
                "data": [o.to_json() for o in self.data],
                "value": self.value()
            }

    @staticmethod
    def package_string_parser(string):
        packages = []

        if string[0] == '1':
            package_count = int(string[1:12], 2)
            
            active_string = string[12:]

            for i in range(package_count):
                if not(Package.bit_string_is_valid_package(active_string)): 
                    break
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
            
        if active_string == '0000000':
            print("added a '0000000' string")
            new_package = Package(0, 0, '00000')
            packages.append(new_package)
            active_string = ''

        return packages, active_string

    @staticmethod
    def value_string_parser(string):
        data = ""
        
        while len(string) > 4:
            data += string[1:5]
            start_bit = string[0]

            string = string[5:]

            if start_bit == '0':
                break
        
        return data, string

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

    @staticmethod
    def version_counter(data_object):
        v_cnt = data_object.version
        if data_object.id != 4:
            for sub_p in data_object.data:
                v_cnt += Package.version_counter(sub_p)

        return v_cnt


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
    n_string = ""
    
    for char in string:
        n_string += HEX_MAP[char]

    return n_string


if __name__ == "__main__":
    strings = []
    data_objects = []

    with open("/Users/jonasvandenbulcke/Documents/reps/advent_of_code_2021/data/day_16.txt", 'r') as input_data:
        for row in input_data.readlines():
            row = row.strip('\n')
            strings.append(row)
            bit_string = to_bit_string(row)
            # print(bit_string)
            n_package = Package.from_bit_string(bit_string)
            print(n_package.to_json())
            # print(row, Package.version_counter(n_package))
            print(row, n_package.value())
            data_objects.append(n_package)

    # print(strings)
    
    # print(data_objects)