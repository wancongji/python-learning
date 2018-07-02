import json

d = {'a': 123, 'b': ['abc', {'c': 234}], 'd': True, 'e': False, 'f': None}
print(d)


class AA:
    def ser(self):
        return 'AA'


print(json.dumps(d))
print(json.dumps(AA().ser()))
