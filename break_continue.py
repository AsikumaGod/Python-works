i = 1
user = ""
while(i <= 5):
    user = input("Just write any name\n")
    print("Your name is " + user)
    if(user == "john"):
        break
    elif(user == "Adams"):
        continue
    i += 1