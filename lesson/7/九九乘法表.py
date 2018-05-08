# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i, '=', i*j,'\t',end=' ')   # \t制表符
    print()

# 右上角
for i in range(1,10):
    print(' '*11*(i-1), end='')
    for j in range(i,10):
        product = i*j
        if product < 10:
            end = '  '
        else:
            end = ' ' 
        print(i,'*',j, '=', i*j,end=end)
    print()