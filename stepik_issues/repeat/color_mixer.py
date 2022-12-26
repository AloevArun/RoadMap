a, b = str(input()), str(input())
colors = ('красный', 'синий', 'желтый')
if a in colors and b in colors:
    if a == b:
        print(a)
    elif a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('оранжевый')
    elif a == 'желтый' and b == 'синий' or a == 'синий' and b == 'желтый':
        print('зеленый')
else:
    print('ошибка цвета')
