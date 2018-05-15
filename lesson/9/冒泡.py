nums = [2,5,1,6,4,7,9,8]
length = len(nums)
for i in range(length):
    flag = False
    for j in range(length-i-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp
            flag = True
    # 用于提高效率
    if not flag:
        break
print(nums)