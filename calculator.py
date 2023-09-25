#Hehe a python calculator
'''
we take user input first
'''
your_input1 = float(input("Enter your first number: "))
your_input2 = float(input("Enter your second number: "))
operator = input("choose your operator: * / - +: ")

if operator == "*":
    result = your_input1 * your_input2
    print("The result is: ",result)
elif operator == "+":
    result = your_input1 + your_input2
    print("The result is: ",result)
elif operator == "-":
    result = your_input1 - your_input2
    print("The result is: ",result)
elif operator == "/":
    result = your_input1 / your_input2
    print("The result is: ",result)