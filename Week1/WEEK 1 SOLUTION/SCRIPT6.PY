#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.

def char(string, start, end):
    p = string[start:end]

    return p

string = input("Enter a string: ")

start = int(input("Enter the start position (index): "))


end = int(input("Enter the end position (index): "))

p = char(string, start, end)
print("Extracted string:", p)
