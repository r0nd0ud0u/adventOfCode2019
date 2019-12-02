

def machine_of_turing_ahah(opcode: int, a:int, b:int):
    if opcode == 1:
        return a + b
    elif opcode == 2:
        return a*b


def calculte_First_value(liste_func:list):
    for i in range(0, len(liste_func), 4):
        print(i)
        if liste_func[i] == 99:
            print(liste_func[0])
            return liste_func[0]
        else:
            liste_func[liste_func[i + 3]] = machine_of_turing_ahah(liste_func[i], liste_func[list_nb[i + 1]],
                                                             liste_func[liste_func[i + 2]])


if __name__ == '__main__':
    with open('input', 'r') as file:
        input_file = file.read()
        list_nb_str = input_file.split(',')
        list_nb = list(map(int, list_nb_str))
        list_nb[1] = 12
        list_nb[2] = 2

        calculte_First_value(list_nb)
        calculte_First_value(list_nb)
