#!/bin/python3

import sys

ac = len(sys.argv)
av = sys.argv

if ac < 2:
    print("none")
    sys.exit()
for i in range(1, ac):
    pos = av[i].find("ism")
    if pos == -1:
        print(f"{av[i]}ism")