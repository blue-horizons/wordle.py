import sys
import time


def clearLine():
    # cursor back????
    sys.stdout.write("\u001b[{n}D")
    sys.stdout.flush()
    print("\b")


test = input("> ")

clearLine()

print("test Complete")
