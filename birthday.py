# This script checks how long you have been on Earth
import datetime
birth_year = int(input("What year were you born: "))
year_now = datetime.datetime.now().strftime('%Y')
your_age = int(year_now) - birth_year
print(f"You are {your_age} years old")
