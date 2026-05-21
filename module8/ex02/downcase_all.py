#!/bin/python3

import sys

ac = len(sys.argv)
av = sys.argv

def downcase_it(s):
    return (s.lower())

if ac < 2:
    print("none")
    sys.exit()
for arg in av:
    print(downcase_it(arg))