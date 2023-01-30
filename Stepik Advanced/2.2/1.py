n = int(input())
squad_1 = 0
squad_2 = 0
squad_3 = 0
squad_4 = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        squad_1 += 1
    elif x < 0 < y:
        squad_2 += 1
    elif x < 0 and y < 0:
        squad_3 += 1
    elif x > 0 > y:
        squad_4 += 1
    else:
        continue
print(f'Первая четверть: {squad_1}',
      f'Вторая четверть: {squad_2}',
      f'Третья четверть: {squad_3}',
      f'Четвертая четверть: {squad_4}',
      sep='\n')