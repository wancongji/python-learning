# 斐波那契数列
x = 1
y = 1
for i in range(1,101):
    if i < 3:
        print(1)
    else:
        sum = x + y
        x = y
        y = sum
        print(sum)