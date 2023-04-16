#lists are a group of elements in python
#list is created by [], separated by commas and enclosed in string signs

currencies =["cedi", "dollars", "naira", "cfa", "yen"]
print(currencies)

#to print from list, use list[element index]..note, they begin from 0

print(currencies[-2])

#you can also combine strings and lists
message = "I love using "
print(message + currencies[1].title() + " everyday")