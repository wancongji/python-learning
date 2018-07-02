from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('G:/python learning/python-learning/lesson/20/my.ini')
print(cfg.sections())

for section in cfg.sections():
    # for key in cfg.options(section):
    #     print(section, key)

    for k, v in cfg.items(section):
        print(k, v)

if not cfg.has_section('test'):
    cfg.add_section('test')

cfg.set()