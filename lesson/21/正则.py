import re

s = '''bottle\nbag\nbig\napple'''
s1 = '''web.master@hotmail.com
test@magedu.com
tom@sina.com
web-master@w.a-com
a@w-a-com
b@a.COM
c@c.cn
gdas@dgsa.net
'''
s2 = '''<a href="www.magedu.com" target='_blank'>马哥<br>教育</a>'''
# for x in enumerate(s):
#     if x[0] % 8 == 0:
#         print()
#     print(x, end=' ')

# print('--match--')
# result = re.match('b', s)
# print(1, result)
#
# result = re.match('a', s)
# print(2, result)

# regex = re.compile('b(\w+)g')
regex = re.compile('(?P<head>b)(\w+)(?P<tail>g)')
regex1 = re.compile('^(\w[\w\.-]*)@(\w[\w\.-]*\.[a-zA-Z]+)', re.M)
regex2 = re.compile('(?<=>)\w+(?=<)')
regex3 = re.compile('<(\w+)([^<>]+)href=(.*)>')

# matchers = regex.finditer(s)
matchers1 = regex1.findall(s1)
# matchers2 = regex2.findall(s2)
matchers3 = regex3.findall(s2)
print(matchers1)
print(matchers3)


# for matcher in matchers:
#     print(matcher)
#     print(matcher.group())
#     print(matcher.group(0))
#     print(matcher.group(1))
#     print(matcher.groups())

# print(regex.sub('test', s))
