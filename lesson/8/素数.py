import math, datetime
lst = [2]
n = 100000
start = datetime.datetime.now()
for i in range(2,n):
    for j in lst:
        if i % j == 0:
            break
        if j >= math.ceil(i**0.5):
            lst.append(i)
            break
    else:
        lst.append(i)
stop = (datetime.datetime.now() - start).total_seconds()
print(len(lst))
# print(lst)
print(stop)