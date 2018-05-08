count = 0
total = 0
while True:
    num = input("输入n个数：")
    if num == 'q' or num == 'Q':
        break

    n = int(num)
    count += 1
    total += n
    aver = total / count
    print(aver)