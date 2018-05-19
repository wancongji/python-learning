import random
nums = []
for _ in range(10):
    nums.append(random.randint(1,20))

lst = [0]*20
for i in nums:
    lst[i-1] += 1
print(lst)

for i in range(len(lst)):
    if lst[i] == 1:
        print("number {} no repeat".format(i))
    elif lst[i] > 1:
        print("number {} repeat {} times".format(i, lst[i]))

