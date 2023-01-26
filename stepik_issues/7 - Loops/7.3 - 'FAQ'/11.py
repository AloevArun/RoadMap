n1 = 1
n2 = 1
n = int(input())
flag = False
for i in range(1, n):
    print(n2, end=' ')
    n2, n1 = n1, n1 + n2
print(n2)
