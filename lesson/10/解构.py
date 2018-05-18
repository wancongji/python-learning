# 从lst = [1,(2,3,4),5]中，提取4出来
lst = [1,(2,3,4),5]
# _,(*_,x),_ = lst
_,[*_,x],_ = lst
print(x)

# JAVA_HOME=/usr/bin
strg = 'JAVA_HOME=/usr/bin'
# name,*_,path = strg.partition('=')
name,*_,path = strg.split('=')
print(name,path)

# [1, 9, 8, 5, 6, 7, 4, 3, 2]冒泡
lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
leng = len(lst)
for i in range(leng):
    flag = False
    for j in range(leng-i-1):
        if lst[j] > lst[j+1]:
            lst[j+1],lst[j] = lst[j],lst[j+1]   # 使用解构
            flag = True
    if not flag:
        break
print(lst)
