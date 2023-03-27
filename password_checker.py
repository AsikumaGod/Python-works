# This script tells you the length of your password
username = input('Enter your username: ')
password = input("Enter your password: ")
passlength = len(password)
hide_pass = passlength * '*'  # converts your password to asterisk

print(f"Dear {username}, your password {hide_pass} is {passlength} characters long")
