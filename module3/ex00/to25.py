#!/bin/python3

ns = input("Enter a numver less than 25\n")

n = int(ns)

if int(n) > 25:
    print("Error")
else :
    while n < 26:
        print(f"Inside the loop, my variable is {n}")
        n += 1
    