# 编写一个函数，能够接收至少2个参数，返回最小值和最大值
# def fn(x,y,*args):
#     big = max(x,y,*args)
#     small = min(x,y,*args)
#     return big,small

# nums = input('Please input some numbers(e.g:1,2,3,...): ').strip().split(',')
# print('maximum is {}，minimum is {}'.format(*fn(*nums)))
        
# 编写一个函数，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐
def triangle_print(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if i < j:
                print(' ' * len(str(j)),end=' ')
            else:
                print(j, end=' ')

        print()

def trangle_print2(n):
    tail = ' '.join([str(i) for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n+1):
        print('{:>{}}'.format(' '.join([str(j) for j in range(i,0,-1)]), width))


n = int(input('Please input a number: ').strip())
# triangle_print(n)
trangle_print2(n)

