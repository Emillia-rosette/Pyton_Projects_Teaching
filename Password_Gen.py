# Password Generator

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

fname = input("what is your name?")

print("Hi", fname)

passwordNum = int(input("How many characters in your password ?"))

pasword = "" .join(random.sample(characters))
print(password)
