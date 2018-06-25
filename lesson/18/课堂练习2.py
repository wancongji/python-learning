def cmds_dispacher():
    # 命令和函数存储的地方
    commands = {}

    # 自定义函数，注册
    def reg(name):
        def _reg(fn):
            commands[name] = fn
            return fn

        return _reg

    def defaultfunc():
        print("Unknown command")

    def dispacher():
        while True:
            cmd = input('>>')
            if cmd.strip() == 'quit':
                return
            commands.get(cmd, defaultfunc)()

    return reg, dispacher


r, d = cmds_dispacher()


# 自定义函数 注册
@r('mag')
def foo1():
    print('welcome mage')


@r('edu')
def foo2():
    print('welcome mage2')


d()
