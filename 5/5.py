import math


class Intcode(object):
    """
    Parses list of ints that make up the intcode program.

    Attributes:
        codes (list): List of ints contain full intcode program
        optcode (int): Determines method called
        commands (set): Mapping of optcodes to method that will be triggered
        index (int): Current index inside of self.codes
        params (list): Params that will be used in methods
        output_index (int): Index inside of self.codes to write output to
    """
    index = 0
    result = 0

    def __init__(self, codes):
        self.codes = codes
        self.optcode = 0
        self.commands = {
            1: self.add,
            2: self.multiply,
            3: self.code_input,
            4: self.code_output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
        }
        while self.index < len(self.codes):
            code = str(self.codes[self.index])
            if len(code) > 2:
                # optcode is always last 2 chars
                optcode = int(code[2:])
                # modes are always the first chars, missing characters default to zero
                modes = [int(i) for i in code.zfill(5)[:3]]
                modes.reverse()
            else:
                optcode = int(code)
                modes = [0, 0, 0, 0]

            if optcode in [1, 2, 7, 8]:
                section = self.codes[self.index:self.index+4]
                self.params = self.get_params(section[1:3], modes)
                self.output_index = section[3]
                self.index += 4
            elif optcode in [3, 4]:
                section = self.codes[self.index:self.index+2]
                self.output_index = section[1]
                self.params = self.get_params([section[1]], modes)
                self.index += 2
            elif optcode in [5, 6]:
                section = self.codes[self.index:self.index+3]
                self.params = self.get_params(section[1:3], modes)
                self.index += 3
            elif optcode == 99:
                self.result = self.codes[0]
                break
            else:
                print(f"Invalid optcode {optcode}")
                break

            self.commands[optcode]()

    def add(self):
        self.codes[self.output_index] = sum(self.params)

    def multiply(self):
        self.codes[self.output_index] = math.prod(self.params)

    def code_input(self):
        self.codes[self.output_index] = int(input("Input: "))

    def code_output(self):
        self.codes[0] = self.params[0]

    def jump_if_true(self):
        if self.params[0]:
            self.index = self.params[1]

    def jump_if_false(self):
        if not self.params[0]:
            self.index = self.params[1]

    def less_than(self):
        if self.params[0] < self.params[1]:
            self.codes[self.output_index] = 1
        else:
            self.codes[self.output_index] = 0

    def equals(self):
        if self.params[0] == self.params[1]:
            self.codes[self.output_index] = 1
        else:
            self.codes[self.output_index] = 0

    def get_params(self, section, modes):
        values = list(zip(section, modes))
        return list(map(self.get_memory, values))

    def get_memory(self, value):
        # Takes a tuple with the value and mode, returns the value using the correct mode
        if value[1] == 0:
            return int(self.codes[value[0]])
        elif value[1] == 1:
            return int(value[0])


with open("input.txt", "r") as f:
    INPUT = list(map(int, f.read().strip().split(',')))

codes = INPUT.copy()

print(Intcode(codes).result)
