from math import log
ln_counter = 0
n = int(input())
for i in range(1, n):
    ln_counter = ln_counter + (1 / (i + 1))
print(ln_counter + 1 - log(n))