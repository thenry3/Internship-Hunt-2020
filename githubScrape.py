from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://github.com/elaine-zheng/summer2020internships")

companies = []
urls = []
locations = []
notes = []

page_content = driver.page_source
soup = BeautifulSoup(page_content, "html.parser")
for internship in soup.select("article table tbody tr"):
    internship_details = internship.find_all("td")

    urls.append(re.findall(
        '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(internship_details[0]))[0])
    companies.append(internship_details[0].get_text())
    locations.append(internship_details[1].get_text())
    notes.append(internship_details[3].get_text())

data = pd.DataFrame({'Company': companies, "Link": urls,
                     "Location": locations, "Notes": notes})
data.to_csv("internships2020.csv", index=False, encoding='utf-8')
