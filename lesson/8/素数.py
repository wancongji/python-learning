import math
lst = [2]
n = 10000
for i in range(2,n):
    for j in lst:
        if i % j == 0:
            break
        if j >= math.ceil(i**0.5):
            lst.append(i)
            break
    else:
        lst.append(i)
print(len(lst))
print(lst)
