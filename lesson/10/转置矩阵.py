lst = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = lst[j][i]
        # print(lst[j][i],end=' ') 
    # print()
print(lst)
