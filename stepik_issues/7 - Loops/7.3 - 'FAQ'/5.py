n = int(input())
total = 1
if n < 13:
    for i in range(1, n+1):
        total *= i
print(total)
