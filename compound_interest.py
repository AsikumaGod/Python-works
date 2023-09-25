#This program calculte compound interest according to the wikipedia formula
#A = P(1 + r/n)**nt
#P = Principal Amount(initialinvestment)
#r = annual nominal interest rate(as a decimal)
#n = number of times the interest is compounded per year
#t = number of years

p = 10000
n = 12
r = 12
t = int(input("Enter the number of years: "))
a = p * (1 + r/n) ** n * t
print(f"Total ampount is ${a}")