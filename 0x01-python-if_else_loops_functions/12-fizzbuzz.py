#!/usr/bin/python3

"""This function prints the numbers from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for numberz in range(1, 101):
        if numberz % 3 == 0 and numberz % 5 == 0:
            print("FizzBuzz ", end="")
        elif numberz % 3 == 0:
            print("Fizz ", end="")
        elif numberz % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numberz), end="")
