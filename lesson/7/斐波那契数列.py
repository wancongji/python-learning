# 斐波那契数列
x = 1
y = 1
i = 1
# for i in range(1,101):
while True:
    if i < 3:
        print(1)
    else:
        sum = x + y
        if sum > 100:
            break
        x = y
        y = sum
        print(sum)
    i += 1