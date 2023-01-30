nums = list(map(int, input().split()))
for num in range(1, len(nums) - 1, 2):
    nums[num], nums[num - 1] = nums[num-1], nums[num]
for num in nums:
    print(num, end=' ')