from pathlib import Path
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list all files')  # 构造解析器
parser.add_argument('path', nargs='?', default='.', help='path help')  # 位置参数，可省略，缺省值为'.'
parser.add_argument('-l', action='store_true')  # 可选参数
parser.add_argument('-a', '--all', action='store_true')



# parser.print_help()


def listdir(path, all=False, detail=False):
    def _getfiletype(f: Path):
        """
        获取文件类型
        :param f:
        :return:
        """
        if f.is_dir():
            return 'd'
        elif f.is_block_device():
            return 'b'
        elif f.is_char_device():
            return 'c'
        elif f.is_symlink():
            return 'l'
        elif f.is_socket():
            return 's'
        else:
            return '-'

    def _getmodestr(mode: int):
        """
        将字符串转化为rwx形式
        :param mode:
        :return:
        """
        modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
        m = mode & 0o777
        # return m, bin(m)
        mstr = ''
        for i, v in enumerate(bin(m)[2:]):
            if v == '1':
                mstr += modelist[i]
            else:
                mstr += '-'
        return mstr

    print(_getmodestr(int('777')))

    def _listdir(path, all=False, detail=False):
        """
        列出文件目录
        :param detail:
        :param path:
        :param all:
        :return:
        """
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):  # 当没给all时，不提供隐藏文件
                continue
            if not detail:
                yield (i.name)
            else:
                # -rwxr-xr-x. 1 root root 154 3月  14 19:27 parameter.sh
                stat = p.stat()
                d = _getfiletype(p)
                mode = oct(p.stat().st_mode)[-3:]
                atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                yield (d, _getmodestr(int(mode)), stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)

    # 排序
    yield from sorted(_listdir(path, all, detail), key=lambda x: x[len(x) - 1])


if __name__ == '__main__':
    args = parser.parse_args()  # 分析参数，同时传入可迭代的参数
    files = listdir(args.path, args.all, args.l)
    print(list(files))
