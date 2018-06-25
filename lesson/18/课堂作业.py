from functools import wraps
import datetime
import time
import inspect


def m_cache(duration):
    def _cache(fn):
        local_cache = {}

        # @wraps
        def wrapper(*args, **kwargs):
            # local_cache有没有过期的key
            def clear_expire():
                expire_keys = []
                for k, (_, ts) in local_cache.items():
                    if datetime.datetime.now().timestamp() - ts > duration:
                        expire_keys.append(k)
                for k in expire_keys:
                    local_cache.pop(k)

            clear_expire()

            # print(args, kwargs)

            def make_key(args, kwargs):
                key_dict = {}  # sorted
                sig = inspect.signature(fn)
                params = sig.parameters  # 这是个有序字典
                param_list = list(params.keys())
                # 位置参数
                for i, v in enumerate(args):
                    # print(i, v)
                    k = param_list[i]
                    key_dict[k] = v
                # 关键字参数
                # for k, v in kwargs:
                #     key_dict[k] = v
                key_dict.update(kwargs)
                # 缺省值处理
                for k in params.keys():
                    if k not in key_dict.keys():
                        key_dict[k] = params[k].default

                return tuple(sorted(key_dict.items()))

            key = make_key(args, kwargs)

            if key not in local_cache.keys():
                ret = fn(*args, **kwargs)
                local_cache[key] = (ret, datetime.datetime.now().timestamp())  # (,,) = key,tuple

            return key, local_cache[key]





        return wrapper
    return _cache


def logger(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)
        return ret

    return wrapper



@logger
@m_cache(6)
def add(x: int, y=5) -> int:
    time.sleep(3)
    ret = x + y
    return ret


add(4)
add(4, 5)
add(4, y=5)
add(x=4, y=5)
add(y=5, x=4)
time.sleep(6)
add(4)
add(4, 5)
add(4, y=5)
add(x=4, y=5)
add(y=5, x=4)
