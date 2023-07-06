#Write a python script to enter any number and check its prime or not.

def a(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if a(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

            
