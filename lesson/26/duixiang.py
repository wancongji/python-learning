class MyClass:
    """
    A example class
    """
    x = 'abc'  # 类属性

    def __init__(self):  # 初始化
        print('init')

    def foo(self):  # 类属性foo，也是方法
        return "foo = {}".format(self.x)


class Person:
    x = 'abc'

    def __init__(self, name, age=18):
        self.name = name
        self.y = age

    def show(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y


# mycls = MyClass()  # 实例化，初始化
a = Person('tom')
b = Person('jerry', 20)

print(a.__class__, b.__class__)
print(a.__class__.__qualname__, b.__class__.__name__)

print(sorted(Person.__dict__.items()), end='\n\n')
print(a.__dict__)
print(b.__dict__)

print(isinstance(b, a.__class__))
