import inspect


def add(x: int, y: int, *args, **kwargs) -> int:
    """

    :param x: int
    :param y: int
    :return: int
    """
    return x + y


print(add.__annotations__)
sig = inspect.signature(add)
print(sig)
print('params: ', sig.parameters)
print('return: ', sig.return_annotation)
print(sig.parameters['y'])

print(add(1.1, 2.1))
print(add(4.0, 5.0))
print(add('a', 'v'))
