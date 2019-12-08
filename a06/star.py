def get_key(val, my_dict=None): 
    for key, value in my_dict.items():
        if val in value:
            return key


if __name__ == "__main__":
    with open('input', 'r') as file:
        list_all = list(map(lambda str:str.strip().split(")"), file.readlines()))
        items = dict()

        for i in list_all:
            items.setdefault(i[0], [])
            items[i[0]].append(i[1])

        print(list_all)
        print(items)
        all_dist = 0
        list_YOU_key = []
        list_SAN_key = []
        for j in items.keys():
            for k in items[j]:
                dist = 0
                cur_item = j
                ok = False
                while not ok:
                    dist += 1
                    if cur_item == "COM":
                        ok = True
                    else:
                        tmp_dict = items.copy()
                        if k == "YOU":
                            list_YOU_key.append(cur_item)
                        if k == "SAN":
                            list_SAN_key.append(cur_item)
                        cur_item = get_key(cur_item, tmp_dict)

                all_dist += dist

        print(list_YOU_key)
        print(list_SAN_key)
        list_intersection = [value for value in list_YOU_key if value in list_SAN_key]
        print(list_intersection[0])
        print(list_YOU_key.index(list_intersection[0]) + list_SAN_key.index(list_intersection[0]))


