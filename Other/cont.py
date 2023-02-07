nums = []
is_mult_flag = False

n = int(input())
for _ in range(n):
    nums.append(int(input()))
is_mult = int(input())

for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] * nums[j] == is_mult:
            is_mult_flag = True
            break

print('ДА' if is_mult_flag else 'НЕТ')


