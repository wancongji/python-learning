# lst = [1,4,9,15,2,5,10,15]，生成新列表，列表元素是lst相邻2项的和
lst = [1, 4, 9, 15, 2, 5, 10, 15]
print([lst[i] + lst[i+1] for i in range(len(lst)-1)])

# 打印九九乘法表
[print('{} * {} = {:<4}{}'.format(i,j,i*j,'\n' if i==j else ''),end='') for i in range(1,10) for j in range(1,i+1)]

# 生成ID
import random
print(['{:>04}.{}'.format(i, ''.join([chr(random.randint(97,122)) for _ in range(10)])) for i in range(1,101)])