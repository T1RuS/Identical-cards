import random


def GameTwo():
    num = []
    num.append(random.randint(1, 4))

    while len(num) != 2:
        arg = random.randint(1, 4)
        if num[0] != arg:
            num.append(arg)
    numgo = []
    for i in range(4):
        numgo.append(0)
    for i in range(2):
        p = num[i]
        numgo[p - 1] = 1
    a = ''
    for i in numgo:
        a += str(i)
    return a


def GameThree():
    num = []
    num.append(random.randint(1, 9))
    p = 0
    while len(num) != 3:
        p += 1
        j = 0
        arg = random.randint(1, 9)
        for i in range(len(num)):
            j += 1
            if num[i] == arg:
                j = 0
                break
        if j == len(num):
            num.append(arg)
    numgo = []
    for i in range(9):
        numgo.append(0)

    for i in range(3):
        p = num[i]
        numgo[p - 1] = 1

    a = ''
    for i in numgo:
        a += str(i)
    return a



def GameFour():
    num = []
    num.append(random.randint(1, 16))
    p = 0
    while len(num) != 5:
        p += 1
        j = 0
        arg = random.randint(1, 16)
        for i in range(len(num)):
            j += 1
            if num[i] == arg:
                j = 0
                break
        if j == len(num):
            num.append(arg)
    numgo = []
    for i in range(16):
        numgo.append(0)

    for i in range(5):
        p = num[i]
        numgo[p - 1] = 1
    a = ''
    for i in numgo:
        a += str(i)
    return a
