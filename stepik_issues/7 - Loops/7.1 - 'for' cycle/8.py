m, p, n = float(input()), int(input()), int(input())

for i in range(1, n+1):
    print(i, m)
    m += (m * (p / 100))
