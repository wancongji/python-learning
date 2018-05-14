#   版本一
# triangle = [[1], [1,1]]
# n = 6
# for i in range(2,n):
#     pre = triangle[i-1]
#     cur = [1]
#     #   除去头尾两个1，进行循环 
#     for j in range(0,i-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)

#   版本一改进版
triangle = []
n = 8
for i in range(0,n):
    if i == 0:
        triangle.append([1])
    else:
        pre = triangle[i-1]
        cur = [1]
        #   除去头尾两个1，进行循环 
        for j in range(0,i-1):
            cur.append(pre[j]+pre[j+1])
        cur.append(1)
        triangle.append(cur)
print(triangle)

