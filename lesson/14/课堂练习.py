def foo(xyz=[]):
    xyz.append(1)
    return xyz

a = foo()
print(foo.__defaults__)
print(a)