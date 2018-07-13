import re
import datetime

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

print(d)
