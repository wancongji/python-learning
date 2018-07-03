from pathlib import Path
import argparse


def showdir(path: str = '.', all=False, detail=False, human=False):
    p = Path(path)
    for file in p.iterdir():
        print(type(file.name))
        if not all and file.name.startswith('.'):
            continue

        # -l
        if detail:
            pass
        else:
            yield file.name


parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list all files')  # 构造解析器
parser.add_argument('path', nargs='?', default='.', help='path help')  # 位置参数
parser.add_argument('-l', action='store_true')
parser.add_argument('-a', '--all', action='store_true')
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument('x', type=int, help="the base")
# parser.add_argument('y', type=int, help="the exponent")
# parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
#
# answer = args.square ** 2
# answer2 = args.x * args.y
# if args.verbose:
#     print("The square of {} is {}".format(args.square, answer))
# else:
#     print(answer)

if __name__ == '__main__':
    args = parser.parse_args(('G:\\',))
    parser.print_help()

    print(args)
    print(args.path, args.l, args.all)

    for file in showdir(args.path):
        print(file)

