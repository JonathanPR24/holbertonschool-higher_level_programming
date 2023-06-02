#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(args)

    print("Number of argument(s):", num_args)
    if num_args == 0:
        print(":")
    else:
        print("Argument{}:".format("s" if num_args > 1 else ""))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
