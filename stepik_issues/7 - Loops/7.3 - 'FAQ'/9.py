n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
largest = max(n_list)
n_list.remove(largest)
print(largest, max(n_list), sep="\n")