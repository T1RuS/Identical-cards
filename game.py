import random


def GameTwo():
    a = [1, 1, 2, 2]
    random.shuffle(a)
    num = ''
    for i in a:
        num += str(i)
    return num


def GameThree():
    a = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    random.shuffle(a)
    num = ''
    for i in a:
        num += str(i)
    return num


def GameFour():
    a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
    random.shuffle(a)
    num = ''
    for i in a:
        num += str(i)
    return num


def UnicNum(list, arg):
    one = 0
    two = 0
    three = 0
    four = 0
    for i in list:
        if i == '1':
            one += 1
        elif i == '2':
            two += 1
        elif i == '3':
            three += 1
        elif i == '4':
            four += 1
    if one == arg or two == arg or three == arg or four == arg:
        return '1'
    return '0'
