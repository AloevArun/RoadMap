nums = list(map(int, input().split()))
counter = 0
for num in range(1, len(nums)):
    if nums[num] > nums[num-1]:
         counter+=1
print(counter)