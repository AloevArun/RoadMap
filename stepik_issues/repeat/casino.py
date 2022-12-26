a = int(input())
sector1 = range(1, 11)
sector2 = range(11, 19)
sector3 = range(19, 29)
sector4 = range(29, 37)
if a == 0:
    print('зеленый')
elif a in sector1 or a in sector3:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif a in sector2 or a in sector4:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')
