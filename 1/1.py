def get_fuel(mass):
    return int(int(mass) / 3) - 2


def handle_fuel_mass(fuel):
    total = fuel
    while fuel > 0:
        fuel = get_fuel(fuel)
        if fuel > 0:
            total += fuel
    return total


# Part 1
with open("input.txt", "r") as f:
    fuel = []
    for mass in f.readlines():
        fuel.append(get_fuel(mass))
    print(sum(fuel))

# Part 2
with open("input.txt", "r") as f:
    fuel_total = []
    for mass in f.readlines():
        fuel = handle_fuel_mass(get_fuel(mass))
        fuel_total.append(fuel)
    print(sum(fuel_total))
