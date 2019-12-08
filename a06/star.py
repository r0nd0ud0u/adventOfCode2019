def get_key(val, my_dict=None): 
    for key, value in my_dict.items():
        if val in value:
            return key


if __name__ == "__main__":
    with open('input', 'r') as file:
        list_all = list(map(lambda str:str.strip().split(")"), file.readlines()))
        # list_name = list_all.split(')')
        items = dict()

        for i in list_all:
            items.setdefault(i[0], [])
            items[i[0]].append(i[1])

        print(list_all)
        print(items)

        all_dist = 0
        for j in items.keys():
            ok = False
            dist = 0
            cur_item = j
            for k in items[j]:
                while not ok:
                    dist += 1
                    if cur_item == "COM":
                        ok = True
                    else:
                        tmp_dict = items.copy()
                        cur_item = get_key(cur_item, tmp_dict)

                all_dist += dist

        print(all_dist)


