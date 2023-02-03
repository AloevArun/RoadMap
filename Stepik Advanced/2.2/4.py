nums = list('12345')  # list(map(int, input().split()))
shifted_nums = []

shifted_nums.insert(0, nums[-1])
for num in range(0, len(nums) - 1):
    shifted_nums.append(nums[num])
for num in shifted_nums:
    print(num, end=' ')
