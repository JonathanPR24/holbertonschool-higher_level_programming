#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print(0)
    else:
        total = sum(int(arg) for arg in sys.argv[1:])
        print(total)
