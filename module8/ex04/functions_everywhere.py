#!/bin/python3
import sys

ac = len(sys.argv)
av = sys.argv

def shrink(s):
    return(s[:8])

def enlarge(s):
    lenght = len(s)
    if lenght < 8:
        while lenght < 8:
            s += "Z"
            lenght += 1
    return(s)

if ac < 2:
    print("none")
    sys.exit()

for i in range(1, ac):
    if len(av[i]) < 8:
        print(enlarge(av[i]))
    elif len(av[i]) > 8:
        print(shrink(av[i]))
    else:
        print(av[i])