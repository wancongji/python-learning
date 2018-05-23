lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
length = len(lst)

for i in range(length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = minindex
    for j in range(i + 1, length - i):
        if lst[maxindex] < lst[j]:
            maxindex = j
        if lst[minindex] > lst[-j - 1]:
            minindex = -j - 1

    if lst[maxindex] == lst[minindex]:  # 元素相同
        break
    if i != maxindex:
        lst[maxindex], lst[i] = lst[i], lst[maxindex]
        # 如果最小值被交换过，要更新索引
        if i == minindex or i == length + minindex:
            minindex = maxindex

    if minorigin != minindex:
        lst[minindex], lst[minorigin] = lst[minorigin], lst[minindex]

print(lst)
