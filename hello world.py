import random
secretNum = random.randint(1,10)
for yourguesses in range(1,10):
    yourguess = int(input("Enter a secret number"))
    if yourguess < secretNum:
        print("Your guess is too low")
    elif yourguess > secretNum:
        print("Your guess is too high")
    elif yourguess == secretNum:
        print("You have cracked the code!!!")  