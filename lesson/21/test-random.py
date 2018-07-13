import random
import datetime
import time

# 数据源
def source():
    while True:
        yield datetime.datetime.now(), random.randint(1, 100)


# 获取数据
src = source()
lst = [next(src) for _ in range(3)]


# 处理函数
def handler(iterable):
    return sum(iterable) // len(iterable)

def window(src, handler, width:int, interval:int):

    for field in src:
        pass


