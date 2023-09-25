import requests
from bs4 import BeautifulSoup

country_page = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(country_page.text, "lxml")
full = soup.find("div", class_="col-md-4 country")

country_name = soup.find_all("h3", class_="country-name")
Capital_city = soup.find_all("span", class_="country-capital")
population = soup.find_all("span", class_="country-population")
with open("countries.txt", "w") as cn:
    for i in range(0, len(country_name)):
        cn.writelines(f"{country_name[i].text.strip()}'s capital city is {Capital_city[i].text} and has a population of {population[i].text}\n\n")