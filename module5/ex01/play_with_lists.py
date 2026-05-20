#!/bin/python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
b = []
# b = [b+2 for b in a]
for i in range(len(a)):
    b.append(a[i] + 2)

print("Original List: ", a)
print("New List: ", b)
