#!/bin/python3

def array_of_names(dict):
    return[f"{first.capitalize()} {last.capitalize()}" for first, last in dict.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))