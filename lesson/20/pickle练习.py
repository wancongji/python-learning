from pathlib import Path

import pickle

lst = 'a b c'.split()
d = dict(zip('abc', range(3)))


class AA:
    CCCC = 'abc'

    def __init__(self):
        self.aa = 'cc'

    def show(self):
        print('abc')


aa = AA()

with open('G:\python learning\python-learning\lesson\\20\\pickletest', 'w+b') as f:
    # pickle.dump(lst, f)
    # pickle.dump(d, f)
    pickle.dump(aa, f)

with open('G:\python learning\python-learning\lesson\\20\\pickletest', 'r+b') as f:
    tmp = pickle.load(f)
    tmp.show()
    print(type(tmp))
    print(tmp)
