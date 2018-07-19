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

    def __init__(self, name):
        self.name = name
        pass


# mycls = MyClass()  # 实例化，初始化
a = Person('tom')
b = Person('jerry')
print(a.name, b.name)
