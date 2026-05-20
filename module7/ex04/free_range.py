#!/bin/python3

import sys
# import numpy as np

ac = len(sys.argv)
av = sys.argv
arr = []

if ac != 3:
    print("none")
    sys.exit()
brr = list(range(int(av[1]), int(av[2]) + 1))
print(brr)

# arr = np.arange(int(av[1]), int(av[2]) + 1)
# print(arr)