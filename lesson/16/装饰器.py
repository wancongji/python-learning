from functools import wraps


def logger(fn):
    @wraps(fn)
    def _logger(*args, **kwargs):
        # before
        print("Before")
        ret = fn(*args, **kwargs)
        # after
        print("After")
        return ret

    return _logger


@logger
def add(x, y=7):
    print("call add...")
    return x + y


add(1, 2)
