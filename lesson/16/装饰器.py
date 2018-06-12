import functools


def logger(fn):
    def _logger(*args, **kwargs):
        # before
        print("Before")
        ret = fn(*args, **kwargs)
        # after
        print("After")
        return ret

    return _logger


@logger
def add(x, y):
    print("call add...")
    return x + y


print(add(1, 2))
