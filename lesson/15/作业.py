# 字典扁平化
d = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}
d1 = {}
lst = []


def flat(prefix='', **kwargs):
    for k, v in kwargs.items():
        # print(k, v)
        if isinstance(v, (list, tuple, dict, set)):
            flat(prefix=prefix+k+'.',**v)
        else:
            d1[prefix+k] = v


flat(**d)
print(d1)


# 实现base64编码
