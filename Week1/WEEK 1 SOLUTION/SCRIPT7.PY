#Write a python script to enter any string, replace vowel with its position number.

def vowel(p):
    vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
    a = ""

    for index, char in enumerate(p, start=0):
        if char in vowels:
            a += str(index)
        else:
            a += char

    return a
p = input("Enter a string: ")
a = vowel(p)

print("Modified string:", a)
