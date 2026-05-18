#!/bin/python3

n = input()
if int(n) == 0:
    print("This number is both positive and negative.")
elif int(n) > 0:
    print("This number is positive.")
else:
    print("This number is negative.")