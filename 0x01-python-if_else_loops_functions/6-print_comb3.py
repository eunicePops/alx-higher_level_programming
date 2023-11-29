#!/usr/bin/python3

for firstdigit in range(0, 10):
for secondigit in range(firstdigit + 1, 10):
        if firstdigit == 8 and secondigit == 9:
            print("{}{}".format(firstdigit, secondigit))
        else:
            print("{}{}".format(firstdigit, secondigit), end=", ")
