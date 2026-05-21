#!/bin/python3

def find_the_redheads(dict):
    return[name for name, hair in dict.items() if hair == "red"]

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))