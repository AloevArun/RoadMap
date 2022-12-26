a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
otrezok1 = set(range(a1, b1 + 1))
otrezok2 = set(range(a2, b2 + 1))
otrezok3 = otrezok1.intersection(otrezok2)
if otrezok3:
    if len(otrezok3) != 1:
        print(min(otrezok3), max(otrezok3))
    else:
        print(min(otrezok3))
else:
    print('пустое множество')
