import math


def calculate_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


def calculate_all_fuel_module(mass: int) -> int:
    ok = False
    full_fuel_module = 0
    tmp = mass
    while not ok:
        tmp = calculate_fuel(tmp)
        print(tmp)
        if tmp <= 0:
            ok = True
            tmp = 0
        full_fuel_module += tmp
    return full_fuel_module


if __name__ == '__main__':
    with open('puzzle1', 'r') as file:
        list_mass_str = list(map(str.strip, file.readlines()))
        list_mass = list(map(int, list_mass_str))
        result = sum(map(calculate_fuel, list_mass))
        print(result)
        result2 = sum(map(calculate_all_fuel_module, list_mass))
        print(result2)