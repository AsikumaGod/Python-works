import requests
from bs4 import BeautifulSoup

all_s = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(all_s.text, "lxml")
all_quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
with open("saved_quotes.txt", "w") as sq:
    for i in range(0, len(all_quotes)):
        # print(f"{authors[i].text} once said {all_quotes[i].text}\n")
        sq.writelines(f"{authors[i].text} once said {all_quotes[i].text}\n")