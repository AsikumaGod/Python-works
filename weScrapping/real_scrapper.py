import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    date_posted = job.find("span", class_="sim-posted").text
    if "few" in date_posted:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            req_skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.a["href"]
            print(f"Company Name: {company_name.strip()}\n")
            print(f"Required Skills:{req_skills.strip()}\n")
            print(f"Date Posted:{date_posted.strip()}\n")
            print(f"job Link:{more_info}")