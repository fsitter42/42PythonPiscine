#!/bin/python3

n = input("Enter the first number:\n")
n2 = input("Enter the second number:\n")

res = int(n) * int(n2)

print(f"{n} x {n2} = {res}")

if int(res) > 0:
    print("The result is positive.\n")
elif int(res) < 0:
    print("The result is negative.\n")
else :
    print("The result is positive and negative.\n")