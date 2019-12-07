import numpy as np

def machine_of_turing_ahah(opcode: object, a: object, b: object) -> object:
    if opcode == 1:
        return a + b
    elif opcode == 2:
        return a*b
    return 0


def calculte_First_value(liste_func):
    for i in range(0, len(liste_func), 4):
        if liste_func[i] == 99:
            return liste_func[0]
        else:
            liste_func[liste_func[i + 3]] = machine_of_turing_ahah(liste_func[i], liste_func[liste_func[i+1]],
                                                                   liste_func[liste_func[i+2]])


if __name__ == '__main__':
    with open('input', 'r') as file:
        input_file = file.read()
        list_nb_str = input_file.split(',')
        list_nb = list(map(int, list_nb_str))
        list_tmp = []
        # star 1
        # list_nb[1] = 12
        # list_nb[2] = 2
        #result = calculte_First_value(list_nb)
        #print(result)

        # star 2
        a = np.array(list_nb)
        for k in range(1, 99):
            for j in range(1, 99):
                list_tmp = np.copy(a)
                list_tmp[1] = k
                list_tmp[2] = j
                result = calculte_First_value(list_tmp)
                if result == 19690720:
                    print(k, j)

