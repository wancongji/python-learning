import re
import datetime
from queue import Queue

logline = '''183.69.210.164 - - [07/Apr/2017:09:32:39 +0800] "GET /member/ HTTP/1.1" 302 31 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" '''

pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''
regex = re.compile(pattern)


def extract(line):
    matcher = regex.match(line)
    if matcher:
        return matcher.groupdict()
    # print(regex.findall(logline))


def conver_time(timestr):
    fmtstr = "%d/%b/%Y:%H:%M:%S %z"
    dt = datetime.datetime.strptime(timestr, fmtstr)
    return dt


def convert_request(request: str):
    return dict(zip(('method', 'url', 'protocol'), request.split()))


ops = {
    'datetime': conver_time,
    'status': int,
    'size': int,
    'request': convert_request
}

d = {}
for k, v in extract(logline).items():
    d[k] = ops.get(k, lambda x: x)(v)


# print(d)


def load(path):
    """
    单文件装载
    :param path:
    :return:
    """
    with open(path, 'r') as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                # TODO 不合格数据有多少
                continue


def window(src, handler, width: int, interval: int):
    start = datetime.datetime.strptime('1970/01/01 01:01:01 +0800', '%Y/%m/%d %H:%M:%S %z')
    current = datetime.datetime.strptime('1970/01/01 01:01:02 +0800', '%Y/%m/%d %H:%M:%S %z')
    test = (current - start).total_seconds()
    delta = datetime.timedelta(seconds=width - interval)
    buffer = []

    for x in src:
        if x:
            buffer.append(x)
            current = x['datetime']

        if test >= interval:
            ret = handler(buffer)

            start = current - delta

            # buffer的处理
            buffer = [i for i in buffer if i['datetime'] > current - delta]


def handler(iterable):
    # TODO
    return sum(iterable) // len(iterable)


def donothing_handler(iterable: list):
    print(iterable)
    return iterable


def size_handler(iterable):
    # TODO
    pass


# 分发器
def dispacher():

    def reg():
        pass

    def run():
        pass

    return reg, run


reg, run = dispacher()


# reg注册窗口


window(load('test.log'), donothing_handler, 10, 5)
