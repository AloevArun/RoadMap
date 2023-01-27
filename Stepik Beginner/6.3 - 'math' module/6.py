from math import sqrt

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    print(b / (2 * a) * -1)
else:
    x1 = (-1 * b + sqrt(d)) / (2 * a)
    x2 = (-1 * b - sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
