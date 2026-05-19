#!/bin/python3

import sys

ac = len(sys.argv)
av = sys.argv

if ac != 2:
    print("none")
    sys.exit()
count = 0
for i in range(len(av[1])):
    if av[1][i] == 'z':
        count += 1
        print('z')
        i += 1
if count == 0:
    print("none")

    




    