import math


def calculate_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    with open('puzzle1', 'r') as file:
        list_mass_str = list(map(str.strip, file.readlines()))
        list_mass = list(map(int, list_mass_str))
        result = sum(map(calculate_fuel, list_mass))
        print(result)