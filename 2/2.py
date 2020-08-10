def intcode(codes):
    """
    Parses list of ints that make up the intcode program.

    Args:
        codes (list): List of ints contain full intcode program
    """
    for index in range(0, len(codes), 4):
        # Look by 4 since each command is 4 in length
        section = codes[index:index+4]
        optcode = section[0]
        if optcode == 1:
            # Add 2 params and store it in address of the 3rd
            codes[section[3]] = codes[section[1]] + codes[section[2]]
        elif optcode == 2:
            # Multiply 2 params and store it in address of the 3rd
            codes[section[3]] = codes[section[1]] * codes[section[2]]
        elif optcode == 99:
            break
    return codes[0]


with open("input.txt", "r") as f:
    INPUT = list(map(int, f.read().strip().split(',')))

# Part 1
codes = INPUT.copy()
codes[1] = 12
codes[2] = 2
print(intcode(codes))

# Part 2
for noun in range(0, 99):
    for verb in range(0, 99):
        codes = INPUT.copy()
        codes[1] = noun
        codes[2] = verb
        result = intcode(codes)
        if result == 19690720:
            print(noun, verb)
