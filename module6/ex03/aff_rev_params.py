#!/bin/python3

import sys

ac = len(sys.argv)

if ac == 1:
    print("none")
else:
    while ac > 1:
        print(sys.argv[ac-1])
        ac -= 1


    
    