# 字典扁平化
d = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}


def flat(**kwargs):
    for i in kwargs:
        print(i)
        # for j in i:
        #     print(j)
            # print(type(j))
            # if type(i):
            #     continue
            # else:
            #     print(j)

        # if not i.items():
        #     return  i




flat(**d)
