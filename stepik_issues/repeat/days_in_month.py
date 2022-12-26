month = int(input())
a, b = [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11]
if 0 < month <= 12:
    if month in a:
        print('31')
    elif month in b:
        print('30')
    else:
        print('28')
