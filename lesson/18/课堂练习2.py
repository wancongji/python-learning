from functools import partial
def cmds_dispacher():
    # 命令和函数存储的地方
    cmd_tbl = {}

    # 注册
    def reg(cmd):
        def _reg(fn):
            func = partial(fn)
            cmd_tbl[cmd] = func
            return func

        return _reg

    def defaultfunc():
        print("Unknown command")

    def dispacher():
        while True:
            cmd = input('>>')
            if cmd.strip() == 'quit':
                return
            cmd_tbl.get(cmd, defaultfunc)()

    return reg, dispacher


r, d = cmds_dispacher()


# 自定义函数
@r('mag')
def foo1():
    print('welcome mage')


@r('edu')
def foo2():
    print('welcome mage2')


d()
