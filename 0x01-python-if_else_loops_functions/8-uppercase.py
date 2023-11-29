#!/usr/bin/python3
def uppercase(str):
    for e in str:
        if ord(e) >= 97 and ord(e) <= 122:
            e = chr(ord(e) - 32)
        print("{}".format(e), end="")
    print()
