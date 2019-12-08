import numpy as np


def get_digit(number, n):
    return int(number / 10 ** n) % 10


def machine_of_turing_ahah(opcode: object, a: object, b: object) -> object:
    print("turing")
    print(opcode)
    if opcode == 1:
        print("opcode 1")
        return a + b
    elif opcode == 2:
        print("opcode 2 ")
        return a * b
    print("nada")
    return 0


def get_value_with_param(list_input, input, input_param):
    if input_param == 0:
        return list_input[input]
    if input_param == 1:
        return input


def calculate_output(liste_func, input_instruction):
    i = 0
    while i < len(liste_func):
        opcode = liste_func[i]
        param_1 = 0
        param_2 = 0
        if opcode > 10:
            print(opcode)
            opcode = get_digit(liste_func[i], 0)
            print(opcode)
            param_1 = get_digit(liste_func[i], 2)
            print(param_1)
            param_2 = get_digit(liste_func[i], 3)
            print(param_2)
        if opcode == 3:
            print("opcode 3 ")
            liste_func[liste_func[i+1]] = input_instruction
            print(input_instruction)
            i += 2
        elif opcode == 4:
            print("opcode 4")
            input_instruction = liste_func[liste_func[i + 1]]
            print(input_instruction)
            i += 2
        else:
            if opcode == 2 or opcode == 1:
                value_1 = get_value_with_param(liste_func, liste_func[i + 1], param_1)
                print(value_1)
                value_2 = get_value_with_param(liste_func, liste_func[i + 2], param_2)
                print(value_2)
                print(opcode)
                liste_func[liste_func[i + 3]] = machine_of_turing_ahah(opcode, value_1, value_2)
                print(liste_func[liste_func[i + 3]])
                i += 4

        if liste_func[i] == 99:
            return input_instruction


if __name__ == '__main__':
    with open('input', 'r') as file:
        input_file = file.read()
        list_nb_str = input_file.split(',')
        list_nb = list(map(int, list_nb_str))

        input_value = 1
        output = calculate_output(list_nb, input_value)
        print("final value")
        print(output)
