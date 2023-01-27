n = int(input())
total = 0
for i in range(n):
    if i * i % 10 in (2, 5, 8):
        total += i
print(total)