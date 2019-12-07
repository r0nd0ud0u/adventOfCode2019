def get_digit(number, n):
    return int(number / 10**n) % 10


if __name__ == '__main__':
    #x = 273025
    x = 273025
    y = 767253
    #y = 767253
    password = 0
    digit = -1
    prev_digit = 0

    for i in range(x, y):
        increment = False
        adjacent = False
        more_than_2 = False
        digit = -1
        prev_digit = 0
        for j in range(0, 6):
            prev_digit = digit
            digit = get_digit(i, j)
            if j >= 1:
                if digit > prev_digit:
                    increment = False
                    break
                else:
                     increment = True
                if digit == prev_digit and adjacent == False:
                    adjacent = True
                    # increment = True
                    # more_than_2 = False
                # elif digit == prev_digit and adjacent == True:
                #     increment = False
                #     adjacent = False
                #     more_than_2 = True
                # else:
                #     adjacent = False
                #     increment = True
        if increment  and adjacent:
            password += 1
    print(password)