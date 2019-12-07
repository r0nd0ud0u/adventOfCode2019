def get_digit(number, n):
    return int(number / 10**n) % 10


if __name__ == '__main__':
    #x = 273025
    x = 273025
    y = 767253
    #y = 767253
    password = 0
    digit = -1

    for i in range(x, y):
        adjacent = 1
        double = False
        prev_digit = get_digit(i,0)
        bigger =False

        for j in range(1, 7):
            digit = get_digit(i, j)

            if digit > prev_digit :
                bigger = True

            if digit == prev_digit:
                adjacent += 1
            else:
                if adjacent == 2:
                    double = True
                adjacent = 1

            prev_digit = digit

        if double and not bigger:
            password += 1
    print(password)