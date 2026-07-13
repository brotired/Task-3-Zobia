# Random Password Generator

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password_length = int(input("Enter password length: "))

password = ""

for i in range(password_length):
    random_character = random.choice(characters)
    password = password + random_character

print("Generated Password:", password)
