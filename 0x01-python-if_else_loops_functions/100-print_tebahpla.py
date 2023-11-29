#!/usr/bin/python3

j = 0
for e in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(e - j)), end="")
    j = 32 if j == 0 else 0
