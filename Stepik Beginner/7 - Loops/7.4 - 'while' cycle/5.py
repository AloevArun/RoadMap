n = int(input())
total = n
while True:
    n = int(input())
    if n >= 0:
        total += n
    else:
        print(total)
        break
