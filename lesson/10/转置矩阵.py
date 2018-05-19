lst = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lst)):
    for j in range(i):
        lst[i][j],lst[j][i] = lst[j][i],lst[i][j]
        # print(lst[j][i],end=' ') 
    # print()
print(lst)

# 不对称矩阵
matrix = [[1,2,3],[4,5,6]]
# matrix = [[1,4],[2,5],[3,6]]

# 一次性开辟目标矩阵的目标空间
tm = [0] * len(matrix[0])
for i in range(len(tm)):
    tm[i] = [0] * len(matrix)
print(tm)

for x in range(len(tm)):
    for j in range(len(tm[x])):
        tm[x][j] = matrix[j][x]

print(tm)