#!/bin/python3

def greetings(s="noble stranger"):
    if isinstance(s, int) == 1:
        print("Error! It was not a name.")
    else:
        print(f"Hello, {s}.")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)