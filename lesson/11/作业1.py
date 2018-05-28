# 打印每一位数字及其重复的次数
dic = {}
num = input("Please input a number: ")
for i in num:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)

# 使用解析式打印
[print('{} repeat {} times.'.format(k,v)) for k,v in dic.items()]