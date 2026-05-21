#!/bin/python3

def find_the_redheads(dict):
    return(list(filter(lambda value: dupont_family[value] == "red", dupont_family)))

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))


### return[name for name, hair in dict.items() if hair == "red"]