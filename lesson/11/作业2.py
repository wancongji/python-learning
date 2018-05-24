import random
d = {}
nums = []
for i in range(10):
    # nums.append(random.randint(-1000,1000))
    nums.append(random.randint(0,10))
print(nums)

for j in nums:
    if j not in d.keys():
        d[j] = 1
    else:
        d[j] += 1
print(d)    

d1 = sorted(d.items())
print(d1)
for x in d1:
    print("数字{}出现的次数为{}".format(x[0],x[1]))