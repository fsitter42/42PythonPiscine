#!/bin/python3

import sys
import re

ac = len(sys.argv)
av = sys.argv
count = 0

if ac < 3:
    print("none")
    sys.exit()
else:
    count = len(re.findall(sys.argv[1], sys.argv[2]))
if count > 0:
    print(count)
else:
    print("none")


    
    