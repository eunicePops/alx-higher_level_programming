#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > biggest:
            biggest = my_list[j]

    return (biggest)
