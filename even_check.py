# checks for even numbers
def checker():
    num1 = int(input('Enter your number: '))

    if (num1 % 2 == 0):
        print('Your number is even')
    elif (num1 % 2 != 0):
        print('Your number is odd')


checker()
