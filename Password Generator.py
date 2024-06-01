#PASSWORD GENERATOR
#A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the password.
#Generate Password: Use a combination of random characters to generate a password of the specified length.
#Display the Password: Print the generated password on the screen.

import random
import string

all_char = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        length = int(input("Enter desired password length (minimum 8):"))
        if length >= 8:
            break
        else:
            print("Password length must be at least 8 characters.")
    except ValueError:
        print("Invalid input. Please enter a number.")

password = "".join(random.choice(all_char) for _ in range(length))

print("Your generated password is:", password)
