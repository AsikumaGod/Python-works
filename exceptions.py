# we can handle errors in our program by handling exceptions
try:
    age = int(input("Enter your age: "))
except ValueError:  # handles value error by printing message below
    print("You did not enter a right age ")
