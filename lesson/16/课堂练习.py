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
# def copy_properties(src):
#     def _copy(dst):
#         dst.__name__ = src.__name__
#         dst.__doc__ = src.__doc__
#         dst.__qualname__ = src.__qualname__
#         return dst
#     return _copy

# 装饰器
import functools

def logger(fn):
    # @copy_properties(fn)
    @functools.wraps(fn)
    def _logger(*args, **kwargs):
        """
        This is a wrapper
        :param args:
        :param kwargs:
        :return:
        """
        print('Before')
        ret = fn(*args, **kwargs)
        print('After')
        return ret
    # functools.update_wrapper(_logger, fn)

    return _logger


@logger
def add(x, y):
    """
    This is a function
    return i
    """
    print("call {}, {} + {}".format(add.__name__, x, y))
    return x + y


print(add.__doc__, add.__name__, add.__qualname__, sep='\n')
print(add.__wrapped__)
# print(add(3, 4))
