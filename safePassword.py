#! python3
# import libraries 
import string
import random

# Asking the user how long the password need to be
password_length = int(input('How long do you want the password to be? '))

# Using the string library to collect the characters for the password
password_characters = string.ascii_letters + string.digits + string.punctuation
 
password = []

# Setting the process to run for the length of the password
for x in range(password_length):
    password.append(random.choice(password_characters)) # Creating the password

print(''.join(password))


