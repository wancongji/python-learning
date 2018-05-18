triangle = []
m = 8
k = 3
for i in range(m):
    if i == 0:
        triangle.append([1])
    else:
        pre = triangle[i-1]
        cur = [1]
        for j in range(0,i-1):
            cur.append(pre[j]+pre[j+1])
        cur.append(1)
        triangle.append(cur)
print(cur[k])
