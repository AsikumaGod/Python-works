for i in range(1,300):
    if i % 3 == 0 and i % 5:
        print(i, "is divisible by 3 and 5")
    elif i % 3 == 0:
        print(i, "is divisble by 3")
    elif i % 5 == 0:
        print(i, "is divisible by 5")
    else:
        print(i, "is not divisible by 3 and 5")