import re

# Question 1

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


def name_checker(a_list):
    for name in a_list:
        i = re.match(r"^[\wA-Z]+\s[A-Z]", name)
        if i:
            print(name)
        else:
            print("Invalid name")
    
name_checker(names)
