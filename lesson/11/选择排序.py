lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
length = len(lst)

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if lst[maxindex] < lst[j]:
            maxindex = j

    if i != maxindex:
        lst[maxindex],lst[i] = lst[i],lst[maxindex]

print(lst)