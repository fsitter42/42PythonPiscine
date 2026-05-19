#!/bin/python3

s = input()

print(s.swapcase())

for i in range(len(s)):
    if s[i].islower():
        print(s[i].upper(), end="")
    elif s[i].isupper():
        print(s[i].lower(), end="")
    else:
        print(s[i], end="")
print()