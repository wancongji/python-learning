from functools import wraps
import time
import inspect


def m_cache(fn):
    local_cache = {}

    def wrapper(*args, **kwargs):
        print(args, kwargs)

        key_dict = {}  # sorted
        sig = inspect.signature(fn)
        od = sig.parameters()  # 这是个有序字典

        param_list = list(od.keys())

        # 位置参数
        for i, v in enumerate(args):
            print(i, v)
            k = param_list[i]
            key_dict[k] = v

        # 关键字参数
        # for k, v in kwargs:
        #     key_dict[k] = v
        key_dict.update(kwargs)

        key = tuple(sorted(key_dict.items()))

        if key not in local_cache.keys():
            ret = fn(*args, **kwargs)
            local_cache[key] = ret

        return local_cache[key]

    return wrapper


@m_cache
def add(x: int, y: int) -> int:
    time.sleep(3)
    ret = x + y
    return ret
