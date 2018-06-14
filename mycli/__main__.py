import sys
from .cmodule import MyCli
from .fmodule import f1_function

def main():
    print('call main')
    args = sys.argv[1:]
    for arg in args:
        print('argument :: {}'.format(arg))
    f1_function('test call : {}'.format(args[0]))
    clis = MyCli(args[0])
    clis.call_check()

if __name__ == '__main__':
    main()
