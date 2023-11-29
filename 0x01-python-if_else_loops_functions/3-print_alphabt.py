#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z') + 1):
    if chr(alphabets) != 'e' and chr(alphabets) != 'q':
        print('{:c}'.format(alphabets), end='')
