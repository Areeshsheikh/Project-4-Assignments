import random
import string


def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = '' .join(random.choice(characters) for _ in range(length))
    return password

#user inputs
length =int(input("Enter the length of your desired passwords"))

password = generated_password(length)
print("your desired Generated password:" , password)