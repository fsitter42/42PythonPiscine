#!/bin/python3

import sys

ac = len(sys.argv)
av = sys.argv

if ac != 2:
    print("none")
    sys.exit()

ans = input("What was the parameter? ")
if ans != av[1]:
    print("Nope, sorry...")
else:
    print("Good job!")

    
    