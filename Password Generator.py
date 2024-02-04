#Simple Password Generating Project
#Nupur Kirwai
import random
#here we will take all inputs valid 
uppercase_letters = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols ="()[]{};+:_-/|!@%$&*?"

#considering all the cases true so that we can make a strong password
uppercase, lowercase, numbers, symbol = True, True, True, True

#defining character
character = " "

if uppercase:
    character += uppercase_letters
if lowercase:
    character += lowercase_letters
if numbers:
    character += digits
if symbol:
    character += symbols
else:
    #if no characters are selected, password will be invalid
    print("Invalid selection")

#taking the user input for the password
print("Welcome to random password generator")
length = int(input("Enter the length of the password: "))
#asking user, yes for making a strong password
letters = input("Do you want to include letters?") == "yes"
num = input("Do you want to include numbers?") == "yes"
syms = input("Do you want to include symbols?") == "yes"

password = ''.join(random.choice(character) for _ in range(length))

#Finally printing the password according to the inputs
print("\nGenerated password: ", password)