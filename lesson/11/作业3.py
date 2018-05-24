import random
s = 'abcdefghijklmnopqrstuvwxyz'
d = {}
lst = []
length = len(s)

for _ in range(100):
    x = random.randint(0,length-1)
    y = random.randint(0,length-1)
    a = s[x]
    b = s[y]
    lst.append(a+b)

for i in lst:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
d1 = sorted(d.items(),reverse=True)
print(lst)
print(d1)