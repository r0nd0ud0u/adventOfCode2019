def calcul_min_distance(list_pos):
    list_dist = []
    for i in list_pos:
        dist = abs(i[0]) + abs(i[1])
        list_dist.append(dist)

    result = min(list_dist)
    return result


def increment_point(cmd: str, a, b,c):
    tab = []
    nb = int(cmd[1:])

    if cmd[0] == 'U' or cmd[0] == 'D':
        if cmd[0] == 'U':
            for i in range(1,nb+1):
                        tab.append((a,i+b))
        else:
            for i in range(1,nb+1):
                tab.append((a,b -i))
            nb = -nb
        b += nb
    c += abs(nb)
    if cmd[0] == 'L' or cmd[0] == 'R':
        if cmd[0] == 'R':
            for i in range(1,nb+1):
                tab.append((i+a,b))
        else:
            for i in range(1, nb+1):
                tab.append((a-i,b))
            nb = -nb
        a += nb
    return tab, a, b, c


def calcul_intersection(a: list, b: list):
    intersect = []
    print("debut")
    for (v, j) in a:
        for (k, l) in b:
            if (j == l) and (v == k):
                print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
                intersect.append((k, l))
                break
    return intersect


def calcul_distance(a, b, c):
    c = c + abs(a) + abs(b)
    return c


if __name__ == '__main__':
    with open('input1', 'r') as file1, open('input2', 'r') as file2:
        input_file1 = file1.read()
        list_segments1 = input_file1.split(',')
        print(list_segments1)

        input_file2 = file2.read()
        list_segments2 = input_file2.split(',')
        print(list_segments2)

        array = []
        array2 = []
        list_tmp = []
        distance_1 = []
        distance_2 = []
        pos_X = 0
        pos_Y = 0
        distance = 0
        for i in list_segments1:
            list_tmp, pos_X, pos_Y, distance = increment_point(i, pos_X, pos_Y,distance)
            array.extend(list_tmp)
            distance_1.append(distance)
        pos_X = 0
        pos_Y = 0
        distance = 0
        list_tmp = []
        for f in list_segments2:
            list_tmp, pos_X, pos_Y, distance= increment_point(f, pos_X, pos_Y,distance)
            array2.extend(list_tmp)
            distance_2.append(distance)

        print("fin array1")
        list_intersect = calcul_intersection(array, array2)
        print("fin intersect")
        print(list_intersect)

        min_dist = calcul_min_distance(list_intersect)
        print(min_dist)

        min_path_list = []

        for (x,y) in list_intersect:
            a = array.index((x,y))
            b = array2.index((x, y))
            min_path_list.append(a+b+2)

        min_path = min(min_path_list)
        print(min_path)



