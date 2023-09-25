import random
secret_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10\n" "Make a guess")
for i in range(1, 5):
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Retry,guess too low")
        continue
    elif guess > secret_number:
        print("Retry, guess too high")
        continue
    elif guess == secret_number:
        print("Congrats, you have broken the code")
        break