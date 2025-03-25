#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    arg_count = len(sys.argv) - 1  # Renommé de 'l' à 'arg_count'
    if arg_count == 1:
        print("{:d} argument:".format(arg_count))
    elif arg_count == 0:
        print("{:d} arguments.".format(arg_count))
    else:
        print("{:d} arguments:".format(arg_count))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
