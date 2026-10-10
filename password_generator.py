import random
import string

def make_password(lenth=8):
    characters= string.ascii_letters+string.digits
    password=""
    for i in range(lenth):
        password+=random.choice(characters)
    return password

print(make_password())
print(make_password(12))




