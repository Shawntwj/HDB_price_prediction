from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

import requests
from bs4 import BeautifulSoup

# this file produces link.csv
URL = "https://forums.hardwarezone.com.sg/"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(URL)

csvFile = open("links.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)

time.sleep(2)
results = driver.find_elements_by_xpath("//h3[@class='node-title']/a")
for result in results:
    link = result.get_attribute("href")
    title = result.text
    csvWriter.writerow((title,link))
    print(title)
 