a, b, c = int(input()), int(input()), str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
    