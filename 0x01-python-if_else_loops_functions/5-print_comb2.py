#!/usr/bin/python3
for numberz in range(0, 100):
    if numberz == 99:
        print("{}".format(numberz))
    else:
        print("{:02}".format(numberz), end=", ")
