#n, k = int(input()), int(input())
n, k = 7, 5
num = 0
for i in range(1, n+1):
    num = (num + k) % i
print(num + 1)

