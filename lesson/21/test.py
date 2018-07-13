import datetime

logline = '''183.69.210.164 - - [07/Apr/2017:09:32:39 +0800] "GET /member/ HTTP/1.1" 302 31 "-" "Mozilla/5.0 (Windows 
NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" '''


def conver_time(timestr):
    fmtstr = "%d/%b/%Y:%H:%M:%S %z"
    dt = datetime.datetime.strptime(timestr, fmtstr)
    return dt


def convert_request(request: str):
    return dict(zip(('method', 'url', 'protocol'), request.split()))


names = ['remote', '', '', 'datetime', 'request', 'status',
         'size', '', 'useragent']

ops = [None, None, None, conver_time,
       convert_request, int, int, None, None]

fields = []

flag = False
tmp = ""

xx = logline.split()

for word in xx:

    if not flag:
        if word.startswith('[') or word.startswith('"'):
            tmp = word[1:]
            if word.endswith(']') or word.endswith('"'):
                tmp = word.strip('[]"')
                fields.append(tmp)
            else:
                flag = True
        else:
            fields.append(word)

        continue

    if flag:
        if word.endswith(']') or word.endswith('"'):
            tmp += " " + word[:-1]
            fields.append(tmp)

            tmp = ""
            flag = False
        else:
            tmp += " " + word

        continue

    # lst.append(word)    # []"

d = {}
for i, field in enumerate(fields):
    key = names[i]
    # print(ops[i])
    if ops[i]:
        d[key] = ops[i](field)
    else:
        d[key] = field

print(d)

print(fields)
