nums = []
while len(nums) < 5:
    num = input("Please input a number:").strip().lstrip('0')
    if not num.isdigit():
        continue
    print("The length of {} is {}".format(num,len(nums)+1))
    nums.append(num)
print(nums)

# sort方法排序
lst = nums.copy()
lst.sort()
print(lst)

# 冒泡法排序
for i in range(len(nums)):
    flag = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp
            flag = True
    if not flag:
        break
print(nums)
    