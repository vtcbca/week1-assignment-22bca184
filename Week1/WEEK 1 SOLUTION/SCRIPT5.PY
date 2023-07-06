#Write a python script to enter any string and count vowel.

def vowel(p):
    vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}

    countvowel = 0

    for char in p:
        if char in vowels:
            countvowel += 1

    return countvowel

p = input("Enter a string: ")
countvowel = vowel(p)
print("Number of vowels:", countvowel)
