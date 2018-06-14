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


# print(flat(d))
# print(flat2(d))

# 实现base64编码
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for i in range(0, length, 3):
        if i + 3 <= length:
            triple = src[i:i + 3]
        else:
            triple = src[i:]
            r = 3 - len(triple)
            triple = triple + '\x00' * r

        # print(triple)
        b = int.from_bytes(triple.encode(), 'big')
        # print(hex(b))

        for j in range(18, -1, -6):
            if j == 18:
                index = b >> j
            else:
                index = b >> j & 0x3F

            ret.append(alphabet[index])

        for i in range(1, r + 1):
            ret[-i] = 0x3D

    return bytes(ret)


# print(base64('abcd'))

# base64实现
import base64

print(base64.b64encode('abcd'.encode()))

# 求2个字符串的最长公共子串
str1 = 'abcd'
str2 = 'bcdfghi'


def findit(str1, str2):
    length = len(str1)
    for i in range(length, 0, -1):
        substr = str1[:i]
        print(substr)
        print(str2.find(substr))
        if str2.find(substr) > -1:
            print("{} is the largest".format(substr))
            return substr


findit(str1, str2)
