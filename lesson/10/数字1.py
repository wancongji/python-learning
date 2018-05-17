while True:
    nums = input("请输入一个数字：").strip().lstrip('0')
    if nums.isdigit():
        # nums = int(nums)    # 也可用于消除开头的零
        break
    else:
        print("输入错误，请输入数字!")

# print("这是个{}位数".format(len(nums)))
# for i in nums:
#     print("数字{0},出现过{1}次".format(i,nums.count(i)))

# 判断0-9的数字在字符串中出现的次数，每一次迭代都是用count
counter = [0]*10
for i in range(10):
    counter[i] = nums.count(str(i))
    if counter[i]:
        print("The count of {} is {}".format(i,counter[i]))

# 迭代字符串本身的字符
counter = [0]*10
for i in nums:
    i = int(i)
    if counter[i] == 0:
        counter[i] = nums.count(str(i))
        print("The count of {} is {}".format(i,counter[i]))

# 最简复杂度
counter = [0]*10
for i in nums:
    i = int(i)
    counter[i] += 1

for i in range(len(counter)):
    if counter[i]:
        print("The count of {} is {}".format(i,counter[i]))

lst = list(nums)
lst.reverse()
print(lst)