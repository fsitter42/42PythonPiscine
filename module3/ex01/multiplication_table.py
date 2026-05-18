#!/bin/python3

ns = input("Enter a number\n")
n = int(ns)

j = 0
for i in range(0, 10):
    print(f"{j} x {n} = {j * n}")
    j += 1
