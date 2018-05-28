import random
s = 'abcdefghijklmnopqrstuvwxyz'
d = {}
lst = []
length = len(s)

for _ in range(100):
    # randstr = ''.join(random.sample(s, 2))
    lst.append(''.join(random.choice(s) for _ in range(2)))

for i in lst:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
d1 = sorted(d.items(),reverse=True)
print(lst)
print(d1)