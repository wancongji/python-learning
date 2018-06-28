# 指定一个源文件，实现copy到目标目录
path = 'G:\python learning\python-learning\\test'
dst = 'G:\python learning\python-learning\\test1'


def copyfile(path, dst):
    with open(path) as f:
        file = f.read()

    with open(dst, 'w') as f1:
        f1.write(file)


# 统计文件单词量，不区分大小写，并显示单词重复最多的10个单词
def wordcount(file='sample.txt'):
    chars = '''~!@#$%^&*()_+{}[]|\\/"'=;:.-<>,'''
    charset = set(chars)
    words = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            word = line.split()

            for k, v in zip(word, (1,) * len(word)):
                k = k.strip(chars).lower()
                if len(k) < 1:
                    continue
                start = 0
                for i, c in enumerate(k):
                    if c in charset:
                        if start == i:
                            start = i + 1
                            continue
                        key = k[start:i]
                        words[key] = words.get(key, 0) + 1
                        start = i + 1
                else:
                    key = k[start:]
                    words[key] = words.get(key, 0) + 1

        lst = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for i in range(10):
            print(str(lst[i]).strip("'()").replace("'", ""))
        print(lst)

    return words


print(wordcount())
