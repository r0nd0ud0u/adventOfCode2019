import itertools as it
import numpy as np

def get_digit(number, n):
    return int(number / 10 ** n) % 10


def machine_of_turing_ahah(opcode: object, a: object, b: object) -> object:

    if opcode == 1:
        return a + b
    elif opcode == 2:
        return a * b
    return 0


def get_value_with_param(list_input, input, input_param):
    if input_param == 0:
        return list_input[input]
    if input_param == 1:
        return input


def calculate_output(liste_func, input_instruction, phase_input):
    liste_func[liste_func[1]] = phase_input = phase_input
    i = 2
    while i < len(liste_func):
        opcode = liste_func[i]
        param_1 = 0
        param_2 = 0
        if opcode > 10 and not opcode == 99:
            opcode = get_digit(liste_func[i], 0)
            param_1 = get_digit(liste_func[i], 2)
            param_2 = get_digit(liste_func[i], 3)
        if opcode == 3:
            liste_func[liste_func[i+1]] = input_instruction
            i += 2
        elif opcode == 4:
            input_instruction = liste_func[liste_func[i + 1]]
            i += 2
        elif opcode == 99:
            return input_instruction
        else:
            value_1 = get_value_with_param(liste_func, liste_func[i + 1], param_1)
            value_2 = get_value_with_param(liste_func, liste_func[i + 2], param_2)
            if opcode == 2 or opcode == 1:
                liste_func[liste_func[i + 3]] = machine_of_turing_ahah(opcode, value_1, value_2)
                i += 4
            elif opcode == 5:
                if not value_1 == 0:
                    i = value_2
                else:
                    i += 3
            elif opcode == 6:
                if value_1 == 0:
                    i = value_2
                else:
                    i += 3
            elif opcode == 7:
                if value_1 < value_2:
                    liste_func[liste_func[i + 3]] = 1
                else:
                    liste_func[liste_func[i + 3]] = 0
                i += 4
            elif opcode == 8:
                if value_1 == value_2:
                    liste_func[liste_func[i + 3]] = 1
                else:
                    liste_func[liste_func[i + 3]] = 0
                i += 4

    return input_instruction


if __name__ == '__main__':
    with open('input', 'r') as file:
        input_file = file.read()
        list_nb_str = input_file.split(',')
        list_nb = list(map(int, list_nb_str))

        x = [0,1,2,3,4]
        list_phases = list(it.permutations(x, 5))
        print(list_phases)

        signal_list = []

        for phase_list in list_phases:
            input_inst = 0
            for phase in phase_list:
                tmp_list = np.copy(list_nb)
                input_inst = calculate_output(tmp_list,input_inst,phase)
                signal_list.append(input_inst)
        print(max(signal_list))

