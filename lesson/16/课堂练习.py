# sorted
def sort(iterable, key=None, reverse=False):
    ret = []
    if key is None:
        key = lambda a, b: a < b

    for x in iterable:
        for i, y in enumerate(ret):
            if key(x, y):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


# lst = [1, 23, 4, 5, 62, 2]
# print(sort(lst, reverse=True))

# 复制属性
def copy_properties(fn):
    def wrapper(src, dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
    return wrapper

# 装饰器
@copy_properties
def logger(fn):
    def _logger(*args, **kwargs):
        print('Before')
        ret = fn(*args, **kwargs)
        print('After')
        return ret

    # copy_properties(fn, _logger)
    return _logger


@logger
def add(x, y):
    """
    This is a function
    return i
    """
    print("call {}, {} + {}".format(add.__name__, x, y))
    return x + y


print(add.__doc__)
print(add(3, 4))
