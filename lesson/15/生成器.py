def gen():
    print('line 1')
    yield 1
    print('line 2')
    # return 2
    yield 2
    print('line 3')
    return 3


next(gen())
next(gen())
g = gen()
print(next(g))
print(next(g))
# print(next(g))
print(next(g, 'End'))


def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i

    c = counter()
    return lambda: next(c)


foo = inc()
print(foo())
print(foo())
print(foo())
