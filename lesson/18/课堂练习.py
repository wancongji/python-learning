import inspect
from functools import wraps


def check(fn):
    @wraps
    def wrapper(*args, **kwargs):
        # 实参检查
        print(args, kwargs)
        sig = inspect.signature(fn)
        params = sig.parameters  # 有序字典

        # 位置参数处理
        param_list = list(params.keys())
        for i, v in enumerate(args):
            k = param_list[i]
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                errstr = "{} {} {}".format(v, 'is not', params[k].annotation)
                print(errstr)
                raise TypeError(errstr)

        # 关键字传参处理
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                errstr = "{} {} {}".format(v, 'is not', params[k].annotation)
                print(errstr)
                raise TypeError(errstr)

        ret = fn(*args, **kwargs)
        return ret

    return wrapper


@check
def add(x: int, y: int = 7) -> int:
    return x + y


add(4)

# print(add.__annotations__)
# sig = inspect.signature(add)
# print(sig)
# print('params: ', sig.parameters)
# print('return: ', sig.return_annotation)
# print(sig.parameters['y'])
# print(inspect.isgenerator(add))

# print(add(1.1, 2.1))
# print(add(4.0, 5.0))
# print(add('a', 'v'))
