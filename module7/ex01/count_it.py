#!/bin/python3

import sys
ac = len(sys.argv)
av = sys.argv

if ac < 2:
    print("none")
    sys.exit()

print(f"parameters: {ac - 1}")
for i in range(ac - 1):
    print(f"{av[i + 1]}: {len(av[i + 1])}")
    