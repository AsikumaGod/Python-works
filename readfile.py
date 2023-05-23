file = open("hyperskill.txt", "r")
i = 0
for files in file.readlines():
    if "summer\n" in files:
        i += 1
        print(i)
file.close()
