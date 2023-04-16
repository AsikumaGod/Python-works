# This script generates random password with your custom length
import random
import string
chars = '!@#$&?' + string.ascii_letters + string.digits
print("Welcome to Password generator\n==================")
amount = int(input("Enter password length:"))
passwd = "".join(random.choice(chars) for i in range(amount))
print(passwd)
