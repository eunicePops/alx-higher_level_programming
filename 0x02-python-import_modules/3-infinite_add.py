#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    sumz = 0
    for j in range(len(sys.argv) - 1):
        sumz += int(sys.argv[j + 1])
    print("{}".format(sumz))
