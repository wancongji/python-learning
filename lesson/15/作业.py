# 字典扁平化
d = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}


def flat(src, dst=None, prefix=''):
    if dst is None:
        dst = {}
    for k, v in src.items():
        # print(k, v)
        if isinstance(v, (list, tuple, dict, set)):
            flat(v, dst, prefix=prefix + k + '.')
        else:
            dst[prefix + k] = v
    return dst


def flat2(src):
    def _flat(src, dst=None, prefix=''):
        for k, v in src.items():
            if isinstance(v, (list, tuple, dict, set)):
                _flat(v, dst, prefix=prefix + k + '.')
            else:
                dst[prefix + k] = v

    dst = {}
    _flat(src, dst)
    return dst


print(flat(d))
print(flat2(d))

# 实现base64编码
