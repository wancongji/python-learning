while True:
    nums = input("请输入一个数字：").strip().lstrip('0')
    if nums.isdigit():
        nums = int(nums)    # 也可用于消除开头的零
        break
    else:
        print("输入错误，请输入数字!")

print("这是个{}位数".format(len(nums)))
for i in nums:
    print("数字{0},出现过{1}次".format(i,nums.count(i)))

lst = list(nums)
lst.reverse()
print(lst)