if __name__ == "__main__":
    with open('input','r') as file:
        width = 25
        height = 6
        input_file = file.read()
        print(input_file)
        size_layer = width * height
        nb_of_zero = 0
        nb_of_one = 0
        nb_of_two = 0
        list_zero_layers = []
        list_product_1_and_2 = []
        j = 1
        for i in input_file:
            if i == '0':
                nb_of_zero += 1
            if i == '1':
                nb_of_one += 1
            if i == '2':
                nb_of_two += 1

            if j < size_layer:
                j += 1
            else:
                list_zero_layers.append(nb_of_zero)
                list_product_1_and_2.append( nb_of_one * nb_of_two )
                nb_of_zero = 0
                nb_of_one = 0
                nb_of_two = 0
                j = 1

        min_zero_index = list_zero_layers.index(min(list_zero_layers))
        print(list_product_1_and_2[min_zero_index])
