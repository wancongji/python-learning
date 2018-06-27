# 指定一个源文件，实现copy到目标目录
# path = 'G:\python learning\python-learning\\test'
# dst = 'G:\python learning\python-learning\\test1'
#
# with open(path) as f:
#     file = f.read()
#
# with open(dst, 'w') as f1:
#     f1.write(file)
#
# print(file)


# 统计文件单词量，不区分大小写，并显示单词重复最多的10个单词
words = []
problem = []
with open('sample.txt', 'rb') as count:
    output = count.read()
    file1 = output.strip().decode().split(' ')

for i in file1:
    if not i.isalpha():
        for j in i.splitlines():
            if j.isalpha():
                words.append(j)
            else:
                problem.append(j)
    else:
        words.append(i)

print(file1)
print(words)
print(problem)
