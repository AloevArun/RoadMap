counter = 0
while True:
    n = int(input())
    if n in range(6):
        if n == 5:
            counter += 1
    else:
        print(counter)
        break
