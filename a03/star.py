def increment_point(x:int, y:int,cmd:str):

    if cmd[0] == 'R':
        x += int(cmd[1:])



if __name__ == '__main__':
    with open('input1', 'r') as file1,  open('input2', 'r') as file2:
        input_file1 = file1.read()
        list_segments1 = input_file1.split(',')
        print(list_segments1)

        input_file2 = file2.read()
        list_segments2 = input_file2.split(',')
        print(list_segments2)

