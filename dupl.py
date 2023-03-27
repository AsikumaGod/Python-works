# this script print duplicates in a set
list_1 = ['a', 'b', 'b', 'c', 'c', 'd', 'a', 'd']
unique = []
duplic = []

for item in list_1:  # checks all items in list_1
    if item not in unique:  # if an item is not in unique set, add it to it
        unique.append(item)
    else:
        duplic.append(item)  # if an item exist already, then add it here

print(unique)
print(duplic)
